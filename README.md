# FX Converter : Currency Conversion Application

<br/>

## Author
`Name:` Lihini Nisansala Dematan Pitiyage 

`Student ID:` 25024175

<br/>

## Description
The FX Converter application can perform currency conversion using data fetched from an open-source API: ` https://www.frankfurter.app/docs/ `. The application is developed using Python and Streamlit.

<br/>

**The application has following key functionalities:**

- Displays the current conversion rate between 2 currency codes for the latest date. 

    `Latest Conversion Rate`

    `The conversion rate on 2023-10-05 from AUD to USD was 0.6349 So 30.0 in AUD correspond to 19.0458 in USD The inverse rate was 1.5752`


- Displays the historical conversion rate between 2 currency codes at a specific date.
  
    `Conversion Rate`

    `The conversion rate on 2023-08-16 from AUD to USD was 0.6461 So 30.0 in AUD correspond to 19.3833 in USD The inverse rate was 1.5477` 

- Calculate the inverse conversion rate between these 2 currencies.
    
    The conversion rate on 2023-08-16 from AUD to USD was 0.6461 So 30.0 in AUD correspond to 19.3833 in USD `The inverse rate was 1.5477`

### Challenges Faced
- The frankfurtur API documentation was not clear on how to use the API endpoints.


### Future Implementations
- Develop a time series conversion data analysis feature using frankfurtur app's time series endpoint.
- Develop a currency rate prediction feature.

<br/>

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>

`Step 01:` Clone the repository

    git clone https://github.com/lihini223/currency-converter.git


Note: To run this application, you need to have Python 3.8 installed on your machine. If you don't have Python 3.8 installed, you can download it from here: https://www.python.org/downloads/release/python-380/ or you can use Anaconda to create a virtual environment with Python 3.8 as follows.

Also, you need to have streamlit, requests, and json packages installed. If you don't have these packages installed, you can install them following the next steps. 


`Step 02:` Create a virtual/Conda environment with the following command.

    conda create -n <env_name> python=3.8

`Step 03:` Create conda environment and Install the required packages with the following command.

    conda create --name <env_name> --file environment.txt


`Step 04:` Try Activating the virtual/Conda environment with the following command.
    
    conda activate <env_name>
    

`Step 05:` Check if the streamlit, requests, and json packages are installed with the following command.
    
    conda list


<br/>


## How to Run the Program
<Provide instructions and examples>

`Step 01:` Activate the virtual/Conda environment with the following command.
    
    conda activate <env_name>

`Step 02:` Run the following command to start the application.    
    
    streamlit run app.py



<br/>


## Project Structure

### `app.py` : 
Contains the main Streamlit python script used for managing users’ inputs and displaying results. In this file, all the UI components are defined.

UI Components:
- `st.title("Fx Converter")` : Displays the title of the application. 
- `st.number_input("Amount to be converted", value=0.00, step=0.01)` : Displays a number input widget for the user to enter the amount of money to be converted.
- `st.selectbox("From Currency", currencies ,placeholder="Select a currency")` : Displays a selectbox widget for the user to select the currency code of the amount of money to be converted and to.
- `st.selectbox("To Currency", currencies ,placeholder="Select a currency")` : Displays a selectbox widget for the user to select the currency code of the amount of money to be converted to.
- `st.button("Get Latest Rates")` : Displays a button widget for the user to get the latest conversion rate between the 2 currencies.
- `st.date_input("Select Date", value=datetime.date.today(), min_value=None, max_value=None, key=None)` : Displays a date input widget for the user to select a date to get the historical conversion rate between the 2 currencies.
- `st.button("Get Historical Rates")` : Displays a button widget for the user to get the historical conversion rate between the 2 currencies.

Also, in this file, the functions for fetching data from the API and calculating the conversion rates are called accordingly.

In the beginning of the file, the following code is used to fetch the currency codes from the API and store them in a list.

    currencies = get_currencies_list() 

Note: `get_currencies_list()` is a function defined in `currency.py` file.

After fetching the list of currencies, check if the list of available currencies is empty, before executing the user inputs.

```
if currencies is None:
    st.error("Error retrieving list of available currencies from Frankfurter API") 
```

Check that the date selected is not in the future to get the historical conversion rate.

```
if input_date > datetime.date.today():
    st.error("Date cannot be in the future")
```

<br/>


### `api.py` :

This file contains the function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string.

```
def get_url(url: str):
    try:
        response = requests.get(url)
        return response.status_code, response.text
    except Exception as e:
        return 500, str(e)
```

<br/>

### `frankfurter.py` :

This file contains the functions used for calling relevant Frankfurter endpoints and extracting information.

`get_currencies_list()` : This function calls the Frankfurter API's currencies endpoint and returns a list of available currencies.

    Endpoint: https://www.frankfurter.app/docs/#currencies


`get_latest_rate(from_currency: str, to_currency: str)` : This function calls the Frankfurter API's latest endpoint and returns the conversion rate between the 2 currencies.

    Endpoint: https://www.frankfurter.app/docs/#latest

`get_historical_rate(from_currency: str, to_currency: str, date: str)` : This function calls the Frankfurter API's historical endpoint and returns the conversion rate between the 2 currencies at the given date.
    
    Endpoint: https://www.frankfurter.app/docs/#historical


<br/>

### `currency.py` :

This file contains the functions used for calculating the conversion rates.

`def round_rate(rate):` : This function rounds the conversion rate to 4 decimal places.

`def reverse_rate(rate):` : this function will calculate the inverse rate from the provided input rate. It will check if the provided input rate is not equal to zero. If it not the case, it will calculate the inverse rate and round it to 4 decimal places. Otherwise it will return zero.

`def convert_currency(amount, rate):` : Convert the amount from from_currency to to_currency using the provided rate(latest or historical).

`def format_output(date, from_currency, to_currency, rate, amount):` : This function formats the output message to be displayed to the user following the below convention.

    The conversion rate on 2023-08-16 from AUD to USD was 0.6461 So 30.0 in AUD correspond to 19.3833 in USD The inverse rate was 1.5477


<br/>

### `README.md` : 
Contains the project documentation.

<br/>

## Citations
<Provide links to any third party code or tutorials you used in this project.>

- https://www.frankfurter.app/docs/
- https://docs.streamlit.io/en/stable/api.html
- https://www.w3schools.com/python/python_datetime.asp
- https://www.w3schools.com/python/python_json.asp
- [Requests package documentation ](https://docs.python-requests.org/en/master/)
- [README writing](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)