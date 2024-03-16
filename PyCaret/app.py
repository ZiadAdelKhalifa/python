# Import necessary libraries
import pandas as pd
from pycaret.classification import *
from pycaret.regression import *
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from package import load_data, perform_eda, train_model
from sklearn.preprocessing import LabelEncoder


# Function to read data from different file formats
def read_data(file_path, file_format='csv'):
    supported_formats = ['csv', 'excel', 'json']
    if file_format.lower() not in supported_formats:
        raise ValueError(f"Unsupported file format. Supported formats: {', '.join(supported_formats)}.")

    if file_format == 'csv':
        return pd.read_csv(file_path)
    elif file_format == 'excel':
        return pd.read_excel(file_path)
    elif file_format == 'json':
        return pd.read_json(file_path)

# Main function for Streamlit web app
def main():
    st.title("Machine Learning Web App")
    
    # Upload file
    uploaded_file = st.file_uploader("Upload Dataset", type=['csv'])
    
    # If file is uploaded
    if uploaded_file is not None:
        # Load data from uploaded file
        data = read_data(uploaded_file)
        
        if 'Date' in data.columns:
            data.drop(columns=['Date'], inplace=True)
        # Display EDA
        st.subheader("Exploratory Data Analysis")
        st.write(data.head())  # Displaying the first few rows of data
        
        # Train Model
        st.subheader("Model Training")
        target = st.selectbox("Select Target Variable", data.columns)
        exp_reg = setup(data, target=target)
        best_model = compare_models()
        
        # Display the algorithm used
        st.write("Algorithm Used:", best_model)
        
        # Histogram of the target column
        st.subheader("Histogram of Target Column")
        plt.figure(figsize=(8, 6))
        sns.histplot(data[target], kde=True)
        st.pyplot()
        
        # Correlation with the target column
        st.subheader("Correlation with Target Column")
        target_corr = data.corr()[target].sort_values(ascending=False)
        st.write(target_corr)
        
        # Most affected columns in the target column
        st.subheader("Most Affected Columns in Target Column")
        most_affected_columns = target_corr[target_corr.index != target]
        st.write(most_affected_columns)

        # Input values for prediction
        st.subheader("Enter Values for Prediction")
        input_values = {}
        for column in data.columns:
            if column != target:
                value = st.text_input(f"Enter value for {column}")
                input_values[column] = value
        
        # Make prediction
        if st.button("Predict"):
            input_df = pd.DataFrame([input_values])
            prediction = predict_model(best_model, data=input_df)
            st.write("Predicted Value:", prediction.iloc[0])

# Run the main function when the script is executed
if __name__ == "__main__":
    main()