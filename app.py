import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title('🧠 Diabetes Prediction using ML')
st.subheader('Enter your health data:')

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.number_input('Pregnancies', step=1)
with col2:
    Glucose = st.number_input('Glucose')
with col3:
    BloodPressure = st.number_input('Blood Pressure')

with col1:
    SkinThickness = st.number_input('Skin Thickness')
with col2:
    Insulin = st.number_input('Insulin')
with col3:
    BMI = st.number_input('BMI')

with col1:
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
with col2:
    Age = st.number_input('Age', step=1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🔴 The person is diabetic.")
    else:
        st.success("🟢 The person is not diabetic.")
