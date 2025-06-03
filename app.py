import threading
import requests
from fastapi import FastAPI
import uvicorn
import streamlit as st
import time
import backend, frontend
import subprocess

app = backend.app

def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")

def run_streamlit():
    subprocess.run(["streamlit", "run", "frontend.py"])

if __name__ == "__main__":
    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()
    time.sleep(1)
    
    # Run Streamlit in the main thread
    run_streamlit()