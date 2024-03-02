import requests
from functools import lru_cache
import time

# Dictionary to store cached weather data
weather_cache = {}
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = '9afc8ba689304327d6f998a73e4ecc44'

def get_cached_weather(city):
    current_time = time.time()
    cached_data = weather_cache.get(city, None)

    if cached_data is not None:
        # Check if the cached data is still valid (less than 30 minutes old)
        cache_time, _ = cached_data
        if current_time - cache_time < 1800:  # 1800 seconds = 30 minutes
            return cached_data[1]  # Return the cached weather data

    return None  # Return None if no valid cached data exists

def cache_weather(city, data):
    current_time = time.time()
    weather_cache[city] = (current_time, data)

def get_weather(city):
    cached_weather = get_cached_weather(city)
    if cached_weather is not None:
        print("Using cached data")
        data = cached_weather
    else:
        request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
        
        # get request to retrieve data
        response = requests.get(request_url)

        # error checking, status code of 200 means successful
        if response.status_code == 200:
            data = response.json()  # gets json data as python dictionary
        else:
            print("An error occurred", response.status_code, response.text)
            return

        # Process and print the weather data
        weather = data["weather"][0]["description"]  # gets weather description
        temperature = round(data["main"]["temp"] - 273.15, 2)  # gets temp in celsius
        feels_like = round(data["main"]["feels_like"] - 273.15, 2)  # gets the "feels like" temperature
        res = {
            "weather": weather,
            "temperature": temperature,
            "feels_like": feels_like,
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
        }

        # Cache the new weather data
        cache_weather(city, res)
    return res


# Example usage
city = input('Enter a city: ')
print(get_weather(city))