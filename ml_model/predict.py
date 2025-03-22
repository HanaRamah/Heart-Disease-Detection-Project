import joblib
import pandas as pd

def predict_heart_disease(model_path, input_data):
    model = joblib.load(model_path)
    prediction = model.predict(input_data)
    return "High Risk" if prediction[0] == 1 else "Low Risk"

def get_user_input():
    # Taking input from the user for each feature 
    cp_0 = int(input("Is chest pain type 0? (1 for Yes, 0 for No): "))
    thal_2 = int(input("Is thalassemia type 2? (1 for Yes, 0 for No): "))
    thal_3 = int(input("Is thalassemia type 3? (1 for Yes, 0 for No): "))
    ca_0 = int(input("Is coronary artery disease 0? (1 for Yes, 0 for No): "))
    exang = int(input("Do you have exercise induced angina? (1 for Yes, 0 for No): "))
    oldpeak = float(input("Enter depression induced by exercise relative to rest: "))
    thalach = float(input("Enter maximum heart rate achieved: "))
    slope = int(input("Enter slope of the peak exercise ST segment (0, 1, or 2): "))
    cp_2 = int(input("Is chest pain type 2? (1 for Yes, 0 for No): "))
    sex = int(input("Enter sex (1 for male, 0 for female): "))
    ca_2 = int(input("Is coronary artery disease 2? (1 for Yes, 0 for No): "))
    cp_1 = int(input("Is chest pain type 1? (1 for Yes, 0 for No): "))
    ca_1 = int(input("Is coronary artery disease 1? (1 for Yes, 0 for No): "))
    age = float(input("Enter age: "))
    ca_3 = int(input("Is coronary artery disease 3? (1 for Yes, 0 for No): "))
    trestbps = float(input("Enter resting blood pressure: "))
    restecg = int(input("Enter resting electrocardiographic results (0, 1, or 2): "))
    chol = float(input("Enter cholesterol level: "))
    
    # Constructing input data in the exact order expected by the model
    input_data = pd.DataFrame({
        'cp_0': [cp_0], 'thal_2': [thal_2], 'thal_3': [thal_3], 'ca_0': [ca_0], 
        'exang': [exang], 'oldpeak': [oldpeak], 'thalach': [thalach], 'slope': [slope], 
        'cp_2': [cp_2], 'sex': [sex], 'ca_2': [ca_2], 'cp_1': [cp_1], 'ca_1': [ca_1], 
        'age': [age], 'ca_3': [ca_3], 'trestbps': [trestbps], 'restecg': [restecg], 
        'chol': [chol]
    })
    
    return input_data

if __name__ == "__main__":
    model_path = "decision_tree_model.joblib"
    
    # Get user input
    user_data = get_user_input()
    
    # Predict the heart disease risk
    result = predict_heart_disease(model_path, user_data)
    
    print(f"Predicted Risk: {result}")
