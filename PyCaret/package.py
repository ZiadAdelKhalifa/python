#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
from pycaret.classification import *
from pycaret.regression import *

# Function to load data from file
def load_data(file_path):
    return pd.read_csv(file_path)  # You can extend it to support other file formats

# Function to perform exploratory data analysis (EDA)
def perform_eda(data):
    return data.describe()  # Simplified EDA, you can extend it

# Function to train machine learning model
def train_model(data, target):
    if data[target].dtype == 'object':
        exp = setup(data, target=target)
        best_model = compare_models()
    else:
        exp = setup(data, target=target)
        best_model = compare_models(fold=5, sort='R2')
    return best_model


# In[ ]:




