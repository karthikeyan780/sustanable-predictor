
import streamlit as st
import pickle
import numpy as np

# Load model
with open('lrmodel_sustainable.pkl','rb') as file:
    model = pickle.load(file)
    
# Title
st.title("Sustainability Megatron")

# User Inputs
carbon_emissions = st.number_input("Carbon emissions amount: ", min_value = 0.0, format = "%f")
energy_output = st.number_input("Energy Output: ", min_value = 0.0, format = "%f")
renewability_index = st.number_input("Index: ", min_value = 0.0, format = "%f")
cost_efficiency = st.number_input("Cost Efficiency: ", min_value = 0.0, format = "%f")

# Predict
if st.button("Predict"):
    # Prepare the inputs for prediction
    input_data = np.array([[carbon_emissions, energy_output, renewability_index, cost_efficiency]])
    
    prediction = model.predict(input_data)
    
    # Display output
    if prediction[0] == 1:
        st.success("W")
    else:
        st.info("L")