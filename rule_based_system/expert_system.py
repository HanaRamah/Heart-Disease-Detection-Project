# Heart_Disease_Detection/rule_based_system/expert_system.py
from rules import HeartDiseaseExpert, Patient

def get_user_input():
    print("Please enter the following information:")
    try:
        age = int(input("Age: "))
        chol = float(input("Cholesterol level (mg/dL): "))
        bp = float(input("Systolic Blood Pressure (mmHg): "))
        bmi = float(input("BMI: "))
        smoking = input("Do you smoke? (yes/no): ").lower()
        exercise = input("Exercise frequency (regular/rare): ").lower()
        diabetes = input("Do you have diabetes? (yes/no): ").lower()
        family_history = input("Family history of heart disease? (yes/no): ").lower()

        return Patient(
            age=age, chol=chol, bp=bp, bmi=bmi,
            smoking=smoking, exercise=exercise,
            diabetes=diabetes, family_history=family_history
        )
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return None

def main():
    print("Heart Disease Risk Assessment System")
    print("===================================")
    
    patient = get_user_input()
    if patient is None:
        return

    engine = HeartDiseaseExpert()
    engine.reset()
    engine.declare(patient)
    engine.run()

    print("\nRisk Assessment Results:")
    print("-----------------------")
    if engine.risk_assessments:
        print("Factors considered:")
        for assessment in engine.risk_assessments:
            print(f"- {assessment}")
    else:
        print("No specific risk factors identified")
    
    final_risk = engine.assess_risk()
    print(f"\nOverall Risk Level: {final_risk}")
    print(f"Risk Score: {engine.risk_level}")

if __name__ == "__main__":
    main()