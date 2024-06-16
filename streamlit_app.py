import streamlit as st
import joblib
import pandas as pd
import sklearn

# Load the pipeline
pipeline = joblib.load('mushroom_classifier_pipeline.pkl')

# Input form
st.title("Mushroom Classification")
st.write("Enter mushroom features to predict if it's edible or poisonous.")

# # Assume columns from the original dataset for user input
# cols = ['cap-diameter','cap-shape','gill-attachment','gill-color','stem-height','stem-width','stem-color','season']

# # Collect user inputs
# user_input = {}
# for col in cols:
#     user_input[col] = st.text_input(f'Enter {col}:')

# Define the columns
cols = ['cap-diameter', 'cap-shape', 'gill-attachment', 'gill-color', 'stem-height', 'stem-width', 'stem-color', 'season']

# Define ranges for select boxes
cap_shape_options = list(range(0, 6))  # Replace with actual range of cap-shape values if different
gill_attachment_options = list(range(0, 6))  # Replace with actual range of gill-attachment values if different
gill_color_options = list(range(0, 11))  # Replace with actual range of gill-color values if different
stem_color_options = list(range(0, 12))  # Replace with actual range of stem-color values if different

# Collect user inputs
user_input = {}
user_input['cap-diameter'] = st.number_input('Enter cap-diameter:', min_value=0, step=1, format='%d')
user_input['cap-shape'] = st.selectbox('Select cap-shape:', cap_shape_options)
user_input['gill-attachment'] = st.selectbox('Select gill-attachment:', gill_attachment_options)
user_input['gill-color'] = st.selectbox('Select gill-color:', gill_color_options)
user_input['stem-height'] = st.number_input('Enter stem-height:', min_value=0.0, format='%f')
user_input['stem-width'] = st.number_input('Enter stem-width:', min_value=0, step=1, format='%d')
user_input['stem-color'] = st.selectbox('Select stem-color:', stem_color_options)
user_input['season'] = st.number_input('Enter season:', min_value=0.0, format='%f')

# Display the user input
st.write('User Input:')
st.write(user_input)
    
# Convert the user input into a DataFrame
input_df = pd.DataFrame([user_input])

# Predict button
if st.button('Predict'):
    # Use the pipeline to make a prediction
    prediction = pipeline.predict(input_df)
    # st.success(prediction[0])
    # Display the result
    if prediction[0] == '0':
        st.success('The mushroom is Edible.')
    else:
        st.error('The mushroom is Poisonous.')
