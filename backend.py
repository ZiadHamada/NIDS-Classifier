# Standard library imports
from collections import defaultdict
from datetime import datetime, timedelta

# Third-party imports
import numpy as np
import pandas as pd
import pickle
import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader

# Local application imports
from src.schemas.input_output_schema import ClassifierRequest, ClassifierResponse
from src.config import Config

# Constants
API_SECRET_KEY = 'zezo450'

# Rate Limiter Class
class RateLimiter:
    def __init__(self, requests_per_min: int = 10):
        self.requests_per_min = requests_per_min
        self.requests = defaultdict(list)

    def is_rate_limited(self, api_key: str) -> tuple[bool, int]:
        now = datetime.now()
        minute_ago = now - timedelta(minutes=1)
        self.requests[api_key] = [req_time for req_time in self.requests[api_key] if req_time > minute_ago]
        recent_requests = len(self.requests[api_key])
        if recent_requests >= self.requests_per_min:
            return True, 0
        self.requests[api_key].append(now)
        return False, self.requests_per_min - recent_requests - 1

# API Security Setup
header_schema = APIKeyHeader(
    name='X-API-Key',
    auto_error=True
)

rate_limiter = RateLimiter(10)

# Dependency Functions
def verify_api_key(api_key: str = Depends(header_schema)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    is_limited, remaining = rate_limiter.is_rate_limited(api_key)
    if is_limited:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Please try again later"
        )
    return api_key

# FastAPI Application Setup
app = FastAPI(
    dependencies=[Depends(verify_api_key)],
    description="NIDS Classifier"
)

def load_model():
    model_path = os.path.join(Config.MODEL_SAVE_PATH, Config.MODEL)
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file missing: {model_path}")
    
    try:
        with open(model_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise ValueError(f"Failed to load model: {str(e)}")

def load_scaler():
    scaler  = os.path.join(Config.MODEL_SAVE_PATH, Config.SCALER)
    
    if not os.path.exists(scaler):
        raise FileNotFoundError(f"Scaer file missing: {scaler}")
    
    try:
        with open(scaler, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        raise ValueError(f"Failed to load scaler: {str(e)}")


# API Endpoints
@app.post("/predict", response_model=ClassifierResponse)
async def predict(
    request: ClassifierRequest,
    api_key: str = Depends(verify_api_key)
):
    print("Received data:", request.dict())  # Log the parsed data
    """Predict sentiment of input text"""
    # Prepare input data
    try:
        data = np.array([[
            request.L4_SRC_PORT, request.L4_DST_PORT, request.L7_PROTO, request.IN_BYTES, request.DURATION_OUT,
            request.MIN_TTL, request.MAX_TTL, request.LONGEST_FLOW_PKT, request.SRC_TO_DST_AVG_THROUGHPUT,  
            request.ICMP_IPV4_TYPE, request.DNS_QUERY_TYPE        
        ]])
        
        data = pd.DataFrame(data)
        
        # Load and run model
        model = load_model()
        scaler = load_scaler()
        label = model.predict(scaler.transform(np.array(data).reshape(1, -1)))
        confidence = model.predict_proba(scaler.transform(np.array(data).reshape(1, -1)))
        
        
        if isinstance(confidence, np.ndarray):
            confidence = confidence[0].tolist()
            confidence = [float(f"{x:.4f}") for x in confidence]
        print(label, confidence)
        
        return {
        "label": "Benign" if label == 0 else "Attack",  # must match exactly
        "confidence": confidence,  # must match exactly
    }
    except Exception as e:
        print(f"CRASH: {str(e)}")  # Will appear in FastAPI logs
        raise HTTPException(status_code=500, detail=str(e))