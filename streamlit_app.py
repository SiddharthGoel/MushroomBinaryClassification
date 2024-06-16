import streamlit as st
import joblib
import pandas as pd

# Load the pipeline
pipeline = joblib.load('mushroom.joblib')

# Input form
st.title("Mushroom Classification")
st.write("Enter mushroom features to predict if it's edible or poisonous.")

# Assume columns from the original dataset for user input
cols = ['cap-diameter','cap-shape','gill-attachment','gill-color','stem-height','stem-width','stem-color','season']

# Collect user inputs
user_input = {}
for col in cols:
    user_input[col] = st.text_input(f'Enter {col}:')
    
# Convert the user input into a DataFrame
input_df = pd.DataFrame([user_input])

# Predict button
if st.button('Predict'):
    # Use the pipeline to make a prediction
    prediction = pipeline.predict(input_df)
    st.success(prediction[0])
    # Display the result
    if prediction[0] == 'e':
        st.success('The mushroom is Edible.')
    else:
        st.error('The mushroom is Poisonous.')
