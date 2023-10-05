from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():

    """Function that will call the relevant API endpoint from Frankfurter \
    in order to get the list of available currencies."""

    # Endpoint: https://www.frankfurter.app/docs/#currencies

    url = f"{BASE_URL}/currencies"

    status_code, response = get_url(url)

    if status_code == 200:
        return json.loads(response)
    else:
        return None


    
def get_latest_rates(from_currency, to_currency, amount):

    """Function that will call the relevant API endpoint from Frankfurter in order to get the 
    latest conversion rate between the provided currencies. """


    # Endpoint: https://www.frankfurter.app/docs/#latest

    url = f"{BASE_URL}/latest?&from={from_currency}&to={to_currency}"

    status_code, response = get_url(url)

    if status_code == 200:
        response = json.loads(response)
        return response["date"], response["rates"][to_currency]
    else:
        return None, None



def get_historical_rate(from_currency, to_currency, from_date, amount):

    """Function that will call the relevant API endpoint from Frankfurter in order to get 
    the conversion rate for the given currencies and date"""
    
    # Endpoint:  https://www.frankfurter.app/docs/#historical

    url = f"{BASE_URL}/{from_date}?&from={from_currency}&to={to_currency}"

    status_code, response = get_url(url)
    
    if status_code == 200:
        response = json.loads(response)
        return response["rates"][to_currency]
    else:
        return None

