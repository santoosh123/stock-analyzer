import streamlit as st
import pandas as pd
st.title("cars price prediction")
cars_df=pd.read_csv("cars24-car-price.csv")
import pickle

# Load the model
with open('lr_model.pkl', 'rb') as f:
    lr = pickle.load(f)

col1, col2,col3 = st.columns(3)

# dropdown
fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol","LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     100, 5000, step=100)
km_driven = col1.slider("Set the km_driven",
                     500, 380000, step=500)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [5,7])
year = col2.slider("Set the year",
                     2010, 2025, step=1)
mileage=col3.slider("Set the mileage",
                     10, 25, step=1)
max_power=col3.slider("Set the max_power",
                     30, 100, step=1)
## Encoding Categorical features
## Use the same encoding as used during the training. 
encode_dict = {
    "fuel_type": {'Diesel': 0, 'Petrol': 3, 'LPG': 2, 'Electric': 1},
    "transmission_type": {'Manual': 1, 'Automatic': 0}
}
if st.button("Get Price"):
    # predict here

    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]
    input_car=[year,km_driven,mileage,engine,max_power,encoded_fuel_type,encoded_transmission_type,seats]
    with open('sc.pkl', 'rb') as f:
        sc = pickle.load(f)

    input_car_scaled = sc.transform([input_car])
    price = lr.predict(input_car_scaled)[0]

    st.header(round(price,2))


