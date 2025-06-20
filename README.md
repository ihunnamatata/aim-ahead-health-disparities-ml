# aim-ahead-health-disparities-ml

Machine learning project analyzing COVID disparities in cardiovascular patients.

AIM-AHEAD Health Disparities ML (Simulated Demo)

This project replicates the structure and analysis of a real AIM-AHEAD/NCATS ML study on health disparities in COVID-19 mortality among cardiovascular patients. The original research was conducted on secure, real-world electronic health record (EHR) data housed within the NCATS N3C enclave and presented at the AIM-AHEAD AI4Equity Symposium.

⚠️ This public repository uses fully synthetic data for demonstration purposes only. No real patient data is included here.
⸻
Project Overview
– Predict COVID-19 mortality using ML models (logistic regression, random forest)
– Analyze impact of race, sex, vaccination status, and age on outcomes
– Balance classes using SMOTE
– Visualize disparities and feature importance
– Includes a simple Streamlit demo for public interaction
⸻
Quick Start
pip install -r requirements.txt
streamlit run app.py

Or open notebooks/disparities_model_v2.ipynb to explore the code.
⸻
Models Used
– Logistic Regression
– Random Forest
– SMOTE for oversampling
⸻
Features
– ROC curves and classification metrics
– Feature importance visualization
– Streamlit app to simulate predictions by demographic
⸻
Folder Structure
– data/ – Synthetic patient dataset
– notebooks/ – ML analysis notebook
– app.py – Streamlit interface
– output/ – Generated visuals
– assets/ – Screenshots and documentation
⸻
Author

Ihunna Amugo
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering
GitHub: @ihunnamatata
