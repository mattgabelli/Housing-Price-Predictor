import streamlit as st
import numpy as np
import joblib

model = joblib.load("rf_model.pkl")

st.title("Housing Price Prediction")

st.divider()

st.write("To obtain housing price prediction, enter no. of bedrooms and bathrooms, and enter the area (in square feet). Then click the button!")

st.divider()

bedrooms = st.number_input("Enter no. of bedrooms", value = 2, step = 1)
bathrooms = st.number_input("Enter no. of bathrooms", value = 1, step = 1)
area = st.number_input("Enter area in square feet", value = 5000, step = 100)

X = [bedrooms, bathrooms, area]

st.divider()

prediction = st.button("Estimate Price")

st.divider()

if prediction:
    x1 = np.array(X)

    prediction = model.predict([x1])[0]

    st.write(f"Estimated house price is £{prediction:,.2f}")
else:
    st.write("Please use button to estimate price!")

#"bedrooms", "bathrooms", "area"