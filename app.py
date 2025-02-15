import streamlit as st
import tensorflow 
from tensorflow.python.keras.models  import load_model


import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder
import pickle

#Load the trained model
model = tensorflow.keras.load_model('model.h5')


#Load the encoders and scalers
with open('onehot_encoder_geo.pkl','rb') as file:
    onehot_encoder_geo = pickle.load(file)
    
    
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)
    
with open('scalar.pkl','rb') as file:
    scalar = pickle.load(file)
    
st.title("Customer Churn Prediction")

geography = st.selectbox("Geography",onehot_encoder_geo.categories_[0])
gender = st.selectbox("Gender",label_encoder_gender.classes_) 
age = st.slider("Age",18,92)
balance = st.number_input("Balance")
credit_score = st.number_input("Credit Score")
estimated_salary = st.number_input("Estimated Salary")
tenure = st.slider("Tenure",0,10)
num_of_products = st.slider("Number of Products",0,4)
has_cr_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])

input_data = pd.DataFrame({
    "Credit Score" : [credit_score],
    "Gender" : [label_encoder_gender.transform([gender])[0]],
    "Age" : [age],
    "Tenure" : [tenure],
    "Balance" : [balance],
    "NumberofProducts" : [num_of_products],
    "HasCrCard" : [has_cr_card],
    "IsActiveMember" : [is_active_member],
    "EstimatedSalary" : [estimated_salary],
})

geo_encoded = onehot_encoder_geo.transform([['Geography']]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded,columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

input_data = pd.concat([input_data.reset_index(drop=True),geo_encoded_df],axis=1)

input_data_scaled = scalar.transfrom(input_data)

prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

if prediction_proba>0.5:
    st.write("The customer is likely to churn")
    
else:
    st.write("The customer is not likely to churn")
