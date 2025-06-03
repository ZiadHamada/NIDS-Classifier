import streamlit as st
from backend import *
    
import requests

# FastAPI backend URL (update if hosted elsewhere)
FASTAPI_URL = "http://127.0.0.1:8000/predict"  # Default local URL
API_KEY = "zezo450"  # Must match your FastAPI secret key

# Streamlit UI
st.title("NIDS Classifier 🚀")
st.markdown("""This app sends network traffic data to a **FastAPI** backend for classification.""")

# Input form
with st.form("input_form"):
    st.subheader("Enter Network Traffic Features")

    # Numeric inputs (matching your ClassifierRequest schema)
    L4_SRC_PORT = st.number_input("L4_SRC_PORT", min_value=0, value=5000)
    L4_DST_PORT = st.number_input("L4_DST_PORT", min_value=0, value=80)
    L7_PROTO = st.number_input("L7_PROTO", min_value=0, value=6)
    IN_BYTES = st.number_input("IN_BYTES", min_value=0, value=100)
    DURATION_OUT = st.number_input("DURATION_OUT", min_value=0.0, value=0.5)
    MIN_TTL = st.number_input("MIN_TTL", min_value=0, value=64)
    MAX_TTL = st.number_input("MAX_TTL", min_value=0, value=64)
    LONGEST_FLOW_PKT = st.number_input("LONGEST_FLOW_PKT", min_value=0, value=10)
    SRC_TO_DST_AVG_THROUGHPUT = st.number_input("SRC_TO_DST_AVG_THROUGHPUT", min_value=0.0, value=100.0)
    ICMP_IPV4_TYPE = st.number_input("ICMP_IPV4_TYPE", min_value=0, value=0)
    DNS_QUERY_TYPE = st.number_input("DNS_QUERY_TYPE", min_value=0, value=1)
    
    submitted = st.form_submit_button("Predict")

# When form is submitted
if submitted:
    # Prepare request data (matches FastAPI's ClassifierRequest)
    data = {
        "L4_SRC_PORT": L4_SRC_PORT,
        "L4_DST_PORT": L4_DST_PORT,
        "L7_PROTO": L7_PROTO,
        "IN_BYTES": IN_BYTES,
        "DURATION_OUT": DURATION_OUT,
        "MIN_TTL": MIN_TTL,
        "MAX_TTL": MAX_TTL,
        "LONGEST_FLOW_PKT": LONGEST_FLOW_PKT,
        "SRC_TO_DST_AVG_THROUGHPUT": SRC_TO_DST_AVG_THROUGHPUT,
        "ICMP_IPV4_TYPE": ICMP_IPV4_TYPE,
        "DNS_QUERY_TYPE": DNS_QUERY_TYPE
    }

    # Send request to FastAPI
    headers = {"X-API-Key": API_KEY}
    try:
        response = requests.post(FASTAPI_URL, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction Successful!")
            
            # Display results
            st.subheader("Results")
            st.write(f"**Label:** {result['label']}")
            st.write(f"**Confidence:** {result['confidence']}")
            
        elif response.status_code == 429:
            st.error("⏳ Rate limit exceeded. Try again later.")
        else:
            st.error(f"❌ Error: {response.text}")
    except Exception as e:
        st.error(f"🚨 Failed to connect to the API: {e}")
        
