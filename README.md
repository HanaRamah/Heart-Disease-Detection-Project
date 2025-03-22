# Heart Disease Detection Project

## Overview
This project implements a Heart Disease Detection System using a rule-based expert system (Experta) and a Decision Tree Classifier (Scikit-Learn). It includes data preprocessing, visualization, and a Streamlit UI for user interaction.

## Setup Instructions
1. Clone the repository: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run preprocessing: `python utils/data_processing.py`
4. Train the model: `python ml_model/train_model.py`
5. Run the  app: ` streamlit run ui/app.py`

## Usage
- Explore data: Open `notebooks/data_analysis.ipynb` in Jupyter.
- Run expert system: `python rule_based_system/expert_system.py`
- Make predictions: Use `ml_model/predict.py` or the Streamlit UI.