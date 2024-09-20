import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model from a pickle file
pickle_in = open("model.pkl", "rb")
classifier = pickle.load(pickle_in)

# Function to make predictions
def predict_transmissibility(PERMX, PERMY, PERMZ, PORO): 

    """
    Predict the oil, gas, and water production based on input features.
    
    Parameters:
    - PERMX: Permeability in X direction
    - PERMY: Permeability in Y direction
    - PERMZ: Permeability in Z direction
    - PORO: Porosity
    
    Returns:
    - Predicted Transmissibility value
    """

    input_features = np.array([[PERMX, PERMY, PERMZ, PORO]])
    prediction = classifier.predict(input_features)
    return prediction

# Main function to display the app interface
def main():
    # Set the title and introduction
    st.title("Oil, Gas, and Water Production Predictor")
    st.markdown("""
    <div style="background-color:#FF6347;padding:10px;">
    <h2 style="color:white;text-align:center;">Reservoir Simulations Model App</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Input fields for user to input reservoir parameters
    PERMX = st.number_input("Permeability in X direction (PERMX)", min_value=0.0, value=0.0, format="%.2f")
    PERMY = st.number_input("Permeability in Y direction (PERMY)", min_value=0.0, value=0.0, format="%.2f")
    PERMZ = st.number_input("Permeability in Z direction (PERMZ)", min_value=0.0, value=0.0, format="%.2f")
    PORO = st.number_input("Porosity (PORO)", min_value=0.0, max_value=1.0, value=0.0, format="%.2f")
    
    result = ""
    
    # Predict button
    if st.button("Predict Transmissibility"):
        # Validate inputs
        if PERMX <= 0 or PERMY <= 0 or PERMZ <= 0:
            st.error("Permeability values must be greater than 0.")
        elif not (0.0 < PORO <= 1.0):
            st.error("Porosity must be between 0 and 1.")
        else:
            result = predict_transmissibility(PERMX, PERMY, PERMZ, PORO)
            st.success(f'The predicted Transmissibility is: {result[0]:.2f}')
    
    # About button
    if st.button("About"):
        st.text("This app predicts the production of oil, gas, and water based on reservoir characteristics.")
        st.text("Built with Streamlit.")

# Run the app
if __name__ == '__main__':
    main()
