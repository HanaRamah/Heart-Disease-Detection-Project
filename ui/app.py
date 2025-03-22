# Heart_Disease_Detection/ui/app.py
import streamlit as st
import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from rule_based_system.rules import Patient , HeartDiseaseExpert


def assess_risk(age, chol, bp, bmi, smoking, exercise, diabetes, family_history):
    try:
        patient = Patient(
            age=float(age),
            chol=float(chol),
            bp=float(bp),
            bmi=float(bmi),
            smoking=smoking.lower(),
            exercise=exercise.lower(),
            diabetes=diabetes.lower(),
            family_history=family_history.lower()
        )
        engine = HeartDiseaseExpert()
        engine.reset()
        engine.declare(patient)
        engine.run()
        return engine.assess_risk(), engine.risk_level, engine.risk_assessments
    except ValueError:
        return "Error", 0, ["Invalid numeric input provided."]

def main():
    st.title("Heart Disease Risk Assessment")
    st.write("Enter your health information to assess your heart disease risk.")

    # Input fields
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    chol = st.number_input("Cholesterol Level (mg/dL)", min_value=0.0, step=1.0)
    bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0.0, step=1.0)
    bmi = st.number_input("BMI", min_value=0.0, step=0.1)
    smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
    exercise = st.selectbox("Exercise frequency", ["Regular", "Rare"])
    diabetes = st.selectbox("Do you have diabetes?", ["No", "Yes"])
    family_history = st.selectbox("Family history of heart disease?", ["No", "Yes"])

    # Assess Risk button
    if st.button("Assess Risk"):
        risk_level, score, factors = assess_risk(age, chol, bp, bmi, smoking, exercise, diabetes, family_history)
        st.subheader("Risk Assessment Results")
        st.write(f"**Overall Risk Level:** {risk_level}")
        st.write(f"**Risk Score:** {score}")
        st.write("**Factors Considered:**")
        if factors:
            for factor in factors:
                st.write(f"- {factor}")
        else:
            st.write("- No specific risk factors identified")

    # Reset button
    if st.button("Reset"):
        st.experimental_rerun()  # Clears inputs by rerunning the app

if __name__ == "__main__":
    main()