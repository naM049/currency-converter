# Import necessary libraries
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv("API_KEY")

# Base URL for the Free Currency API
Base_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


def currency_converter(from_currency, to_currency, amount):
    """
    Convert a specific amount from one currency to other currencies.

    Parameters:
    from_currency (str): The currency to convert from.
    to_currency (list): A list of currencies to convert to.
    amount (float): The amount of currency to convert.

    Returns:
    dict: A dictionary with the conversion rates for the specified currencies.
    """

    currencies = ",".join(to_currency)
    url = Base_URL + f"&base_currency={from_currency}&currencies={currencies}"

    try:
        response = requests.get(url)
    except:
        return "An error occurred while trying to fetch the data."

    
    data = response.json()["data"]

    for key, rate in data.items():
        data[key] = rate * amount

    return data


rates = currency_converter("AUD", ["USD", "GBP", "EUR"], 100)
print(rates)