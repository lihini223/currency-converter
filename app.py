import streamlit as st
# import api.py as api
import requests

st.title("Fx Converter")

# Get user input for amount to be converted
st.number_input("Amount to be converted", value=50.00, step=0.01)


# Get user input for currency to be converted from
st.selectbox("From Currency", ("op1", "op2", "op3"),placeholder="Select a currency",)


# Get user input for currency to be converted to
st.selectbox("To Currency", ("op1", "op2", "op3"),placeholder="Select a currency",)


# button to get latest fx rates
if st.button("Get Latest Rates"):
    st.write("Latest Rates")

# print latest fx rates
st.write("Latest Conversion Rates")


# Get user input for date to get historical fx rates
st.date_input("Select Date", value=None, min_value=None, max_value=None, key=None)


# button to get historical fx rates
if st.button("Get Historical Rates"):
    st.write("Historical Rates")

st.write("Conversion Rate")


# currencies = api.get_currencies()

# st.write(currencies)

response = requests.get("https://api.frankfurter.app/currencies")
currencies = response.json()

st.write(currencies)