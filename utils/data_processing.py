import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def process_data(input_path, output_path):
    # Load dataset
    data = pd.read_csv(input_path)

    # Handle missing values
    data = data.dropna(subset=['restecg'])
    data.fillna({'oldpeak': data['oldpeak'].median()}, inplace=True)

    # Normalize numeric features
    numeric = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    scaler = MinMaxScaler()
    data[numeric] = scaler.fit_transform(data[numeric])

    # Encode categorical variables
    nominal_categorical = ['cp', 'thal', 'ca']
    data = pd.get_dummies(data, columns=nominal_categorical, prefix=nominal_categorical)

    # Feature selection based on correlation
    corr_matrix = data.corr()
    target_corr = corr_matrix['target'].abs().sort_values(ascending=False)
    important_features = target_corr[target_corr > 0.1].index.tolist()
    data = data[important_features]

    # Save cleaned data
    data.to_csv(output_path, index=False)
    return data

if __name__ == "__main__":
    input_path = "/home/hana/Desktop/newproject/data/raw_data.csv"
    output_path = "/home/hana/Desktop/newproject/data/cleaned_data.csv"
    process_data(input_path, output_path)