# -*- coding: utf-8 -*-
"""
Created on Jul 13, 2025
@author: Aditya Bhadauria
"""

import pickle
import streamlit as st

# Load the diabetes prediction model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# App title and layout
st.set_page_config(page_title="Diabetes Prediction", layout="centered")
st.title('Diabetes Prediction using Machine Learning')
st.subheader("Developed by Aditya Bhadauria")

# Input fields
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Age')

# Prediction
diab_diagnosis = ''

if st.button('Predict Diabetes'):
    try:
        input_data = [[
            float(Pregnancies), float(Glucose), float(BloodPressure),
            float(SkinThickness), float(Insulin), float(BMI),
            float(DiabetesPedigreeFunction), float(Age)
        ]]
        diab_prediction = diabetes_model.predict(input_data)

        if diab_prediction[0] == 1:
            diab_diagnosis = '🔴 The person is **diabetic**.'
        else:
            diab_diagnosis = '🟢 The person is **not diabetic**.'
    except:
        diab_diagnosis = '⚠️ Please enter valid numeric values in all fields.'

    st.success(diab_diagnosis)
