# NIDS Classifier

This project designed for Network Intrusion Detection System using **one machine learning models** :DecisionTreeClassifier model. The model is deployed using FastAPI and Streamlit as interface.

---


Report Classification

            precision    recall  f1-score   support

        0       1.00      1.00      1.00    223774
        1       1.00      1.00      1.00     12769

accuracy                            1.00    236543
macro avg       1.00      1.00      1.00    236543
weighted avg    1.00      1.00      1.00    236543

Confusion Matrix
[[223774      0]
 [     0  12769]]


---

## Pipeline Overview

1. **Data Preparation**
   - Cleaned and preprocessed NIDS dataset.

2. **Model Training**
   - Trained  model: DecisionTreeClassifier.

3. **Evaluation**
   - Used classification report and confusion matrix to test model.

4. **Deployment**
    The project is fully deployed using FastAPI:
    - **Web Interface**: Streamlit — for users to detect attackers is found or not.
    - **FastAPI**: `POST /predict` — accepts POST requests.

---

## How to Run Locally

```bash
# Step 1: Create a new environment
conda create -n imdb_env python=3.9
conda activate imdb_env

# Step 2: Install dependencies
pip install -r requirements.txt


# Step 3: Run the app
python app.py


Made with 💙 by **Ziad Hamada**
GitHub: **https://github.com/ZiadHamada**




Information about data
Website of dataset: https://staff.itee.uq.edu.au/marius/NIDS_datasets/

The datasets on this page are designed for machine learning-based Network Intrusion Detection
Systems (NIDS) and are organised into the following high-level collections:

NetFlow V3 Datasets: This collection consists of four datasets in NetFlow format. 
This is the only version incorporating temporal features. These datasets build on the 
43 features of V2 by adding 10 temporal NetFlow features, totaling 53 features.

The NF-UNSW-NB15-v3 dataset is a NetFlow-based version of the well-known UNSW-NB15 dataset, enhanced with additional NetFlow features and labelled according to its respective attack categories. It consists of a total of 2,365,424 data flows, where 127,639 (5.4%) are attack samples and 2,237,731 (94.6%) are benign. The attack flows are categorised into nine classes, each representing a distinct cyber threat. The table below provides a detailed distribution of the dataset:

Class	        Count	        Description
Benign	        2,237,731	Normal unmalicious flows
Fuzzers	        33,816		An attack in which the attacker sends large amounts of random data which cause a system to crash and also aim to discover security vulnerabilities in a system.
Analysis	2,381		A group that presents a variety of threats that target web applications through ports, emails and scripts.
Backdoor	1,226		A technique that aims to bypass security mechanisms by replying to specific constructed client applications.
DoS     	5,980		Denial of Service is an attempt to overload a computer system's resources with the aim of preventing access to or availability of its data.
Exploits	42,748		Are sequences of commands controlling the behaviour of a host through a known vulnerability
Generic 	19,651		A method that targets cryptography and causes a collision with each block-cipher.
Reconnaissance	17,074		A technique for gathering information about a network host and is also known as a probe.
Shellcode	4,659		A malware that penetrates a code to control a victim's host.
Worms   	158		Attacks that replicate themselves and spread to other computers.

# NIDS-Classifier
