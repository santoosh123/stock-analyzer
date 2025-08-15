import streamlit as st
import pandas as pd
import pickle
import sklearn


st.title("Car Resale Price Prediction")

with open('car_pred_model', 'rb') as f:
    model = pickle.load(f)

# sklearn model which is trained on cars24 data.



col1, col2,col3 = st.columns(3)

# dropdown
fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,9,11])
year = col1.slider("Set the year",
                     2010, 2025, step=1)
mileage=col3.slider("Set the mileage",
                     10, 22, step=1)
km_driven = col3.slider("Set the km_driven",
                     500, 300000, step=500)


## Encoding Categorical features
## Use the same encoding as used during the training. 
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


if st.button("Get Price in lakhs"):
    # predict here

    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    input_car = [year,2,km_driven,encoded_fuel_type,encoded_transmission_type,mileage,engine,46.3,seats]
    price = model.predict([input_car])[0]
    if price < 0:
        price = 0.1

    st.header(round(price,2))
st.write("NOTE: This is just an approximate prices. The actual price may differ by +20% or -30% after actual inspection")
