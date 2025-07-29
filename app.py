import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_model.pkl")



st.title("🎓 Student Performance Prediction")
st.markdown("Enter student details to predict **Pass/Fail** outcome")

# Input fields
age = st.number_input("Age", min_value=10, max_value=25, value=17)
studytime = st.slider("Study Time (1=Low, 4=High)", 1, 4, 2)
failures = st.slider("Past Class Failures", 0, 4, 0)
absences = st.number_input("Number of Absences", min_value=0, max_value=100, value=5)
G1 = st.number_input("G1 Grade (0-20)", min_value=0, max_value=20, value=10)
G2 = st.number_input("G2 Grade (0-20)", min_value=0, max_value=20, value=12)

# Prediction
if st.button("Predict Result"):
    input_data = pd.DataFrame([{
        'age': age,
        'studytime': studytime,
        'failures': failures,
        'absences': absences,
        'G1': G1,
        'G2': G2
    }])

    result = model.predict(input_data)
    output = "✅ PASS" if result[0] == 1 else "❌ FAIL"
    st.success(f"Prediction: {output}")
