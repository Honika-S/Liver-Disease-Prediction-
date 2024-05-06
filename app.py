import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open("trained_model.joblib", "rb") as f:
    cb_model = pickle.load(f)

# Title of the web app
st.title("Liver Disease Predictor")

# Input fields for user input
age = st.number_input("Enter age:")
sex = st.selectbox("Select sex:", options=[0,1])
ALB = st.number_input("Enter ALB level:")
ALP = st.number_input("Enter ALP level:")
ALT = st.number_input("Enter ALT level:")
AST = st.number_input("Enter AST level:")
BIL = st.number_input("Enter BIL level:")
CHE = st.number_input("Enter CHE level:")
CHOL = st.number_input("Enter CHOL level:")
CREA = st.number_input("Enter CREA level:")
GGT = st.number_input("Enter GGT level:")
PROT = st.number_input("Enter PROT level:")

# When the user clicks the predict button
if st.button("Predict"):
    # Create input_data containing the user input
    input_data = np.array([[age, sex, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])
    
    # Use your trained model to make predictions
    predicted_disease_type = cb_model.predict(input_data)
    
    # Display prediction
    st.write("Predicted liver disease type:", predicted_disease_type)
    
    # Convert predicted disease type to human-readable format
    # Convert predicted disease type to human-readable format
    disease_types = {0: "Blood Donor", 1: "Hepatitis", 2: "Fibrosis", 3: "Cirrhosis", 4: "Suspect Blood Donor"}

    # Ensure predicted_disease_type is a scalar value
    predicted_disease = predicted_disease_type.item() if isinstance(predicted_disease_type, np.ndarray) else predicted_disease_type

    # Check if the predicted disease type is in the dictionary
    if predicted_disease in disease_types:
        st.write("Predicted disease type:", disease_types[predicted_disease])
    else:
        st.write("Unknown disease type")

