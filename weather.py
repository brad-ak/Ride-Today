import requests


## Function for get request
def perform_request(api_key, location):
    return response


## Pull the API key from a file
with open("weather_api_key", "r") as f:
    api_key = str(f.readline()).strip()


## Base URL for querying the api
url = "https://api.tomorrow.io/v4/timelines"

## Need to come up with a way to get location
location = "33,84"

## Field s to send to the api
query_string = {
    "location":location,
    "fields":["temperature", "cloudCover"],
    "units":"imperial",
    "timesteps":"1h",
    "apikey":api_key
}

## Actual get request
response = requests.request("GET", url, params=query_string)
results = response.json()['data']['timelines'][0]['intervals']


## Parse the information
for daily_result in results:
    date = daily_result['startTime'][0:10]
    temp = round(daily_result['values']['temperature'])
    print("On",date,"it will be", temp, "F")
