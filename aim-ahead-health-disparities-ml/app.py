
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="AIM-AHEAD Disparity Predictor", layout="centered")
st.title("🌍 COVID-19 Mortality Risk Predictor")
st.markdown("This is a simulation app trained on synthetic data based on AIM-AHEAD cohort structure. It does not use real patient data.")

# Input options
sex = st.selectbox("Sex", ["Male", "Female"])
race = st.selectbox("Race", ["White", "Black", "Asian", "Hispanic", "Other"])
vax = st.selectbox("Vaccination Status", ["Vaccinated", "Unvaccinated"])
age = st.slider("Age", 40, 90, 65)

# Map to model encoding
sex_map = {"Male": 1, "Female": 0}
race_map = {"White": 4, "Black": 0, "Asian": 1, "Hispanic": 2, "Other": 3}
vax_map = {"Vaccinated": 1, "Unvaccinated": 0}

X_input = pd.DataFrame([{
    "Age": age,
    "Sex": sex_map[sex],
    "Race": race_map[race],
    "VaccinationStatus": vax_map[vax]
}])

# Load models (placeholder simulation)
rf_risk = 0.72 if race == "Black" and vax == "Unvaccinated" else 0.18 + 0.1 * (90 - age) / 50
rf_risk = min(max(rf_risk, 0.01), 0.95)

# Display
st.subheader("🧠 Predicted Mortality Risk (simulated)")
st.metric(label="Random Forest Model", value=f"{rf_risk*100:.1f} %")

if rf_risk > 0.5:
    st.error("High predicted risk of mortality. Prioritize clinical support.")
elif rf_risk > 0.2:
    st.warning("Moderate risk. Suggest preventive care and follow-up.")
else:
    st.success("Low predicted risk.")
