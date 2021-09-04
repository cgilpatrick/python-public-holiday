import requests
from datetime import date
import os

# Set API key from environment variable
api_key = os.environ.get('ABSTRACT_API_KEY')

# Get the date and parse year, month and day
today = date.today()
year = today.strftime("%Y")
month = today.strftime("%-m")
day_of_month = today.strftime("%-d")

# Make the API request
response = requests.get(f'https://holidays.abstractapi.com/v1/?api_key={api_key}&country=GB&year={year}&month={month}&day={day_of_month}')

# Parse the response code
return_code = response.status_code

if return_code != 200:
  print("Response code is not 200")
  exit

# Parse the response
api_response = response.json()

if api_response:
  holiday = api_response[0]["name"]
  print(f"It's {holiday} today! Enjoy your day!")
else:
  print("Today isn't a public holiday :(")
  exit