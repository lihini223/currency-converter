import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output


st.title("Fx Converter")


# Get the list of available currencies from Frankfurter API
currencies = get_currencies_list()


# Check if the list of available currencies is empty
if currencies is None:
    st.error("Error retrieving list of available currencies from Frankfurter API")


# Input field for capturing amount to be converted
input_amount = st.number_input("Amount to be converted", value=0.00, step=0.01)


# Get user input for currency to be converted from
from_currency = st.selectbox("From Currency", currencies ,placeholder="Select a currency")


# Get user input for currency to be converted to
to_currency = st.selectbox("To Currency", currencies ,placeholder="Select a currency")


# Button to get and display the latest rate for selected currencies and amount
if st.button("Get Latest Rates"):
    latest_date, latest_rate = get_latest_rates(from_currency, to_currency, input_amount)
    if latest_date is None or latest_rate is None:
        st.error("Error retrieving latest conversion rate from Frankfurter API")
    else:
        st.write("Latest Conversion Rate")
        st.write(format_output(latest_date, from_currency, to_currency, latest_rate, input_amount))


# The date selector (calendar) for historical rates
input_date = st.date_input("Select Date", value=datetime.date.today(), min_value=None, max_value=None, key=None)


# Check that the date selected is not in the future
if input_date > datetime.date.today():
    st.error("Date cannot be in the future")
    

# Button to get and display the historical rate for selected date, currencies and amount
if st.button("Get Historical Rates"):
    historical_rate = get_historical_rate(from_currency, to_currency, input_date, input_amount)
    if historical_rate is None:
        st.error("Error retrieving historical conversion rate from Frankfurter API")
    else:
        st.write("Conversion Rate")
        st.write(format_output(input_date, from_currency, to_currency, historical_rate, input_amount))









