import os

from pathlib import Path

def get_project_root() -> Path:
    """Returns the project root folder"""
    return Path(__file__).parent.parent

class Config:
    # Data settings
    DATA_PATH = get_project_root() / 'Data'
    TRAIN_DATA = 'NF-UNSW-NB15-v3.csv'
    
    # Model settings
    MODEL_TYPE = 'decision_tree_classifier'
    MAX_DEPTH = 9
    CRITERION = 'entropy'
    MAX_FEATURES = 0.7
    MIN_SAMPLES_LEAF = 5
    RANDOM_STATE = 0
     
    # Hyperparameters
    
    # Output settings
    MODEL_SAVE_PATH = get_project_root() / 'artifacts'
    MODEL = 'nids_decision_tree_model.pkl'
    COLUMNS = 'nids_columns.pkl'
    SCALER = 'scaler.pkl'