import requests
import json

def fetch_weather_data(lat, long):
    api_key = "<your api key>"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat" : lat,
        "lon" : long,
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def display_weather_data(weather_data):
    if "name" in weather_data:
        if weather_data.get("cod") != "404":
            main_data = weather_data.get("main", {})
            weather = weather_data.get("weather", [{}])[0]

            if main_data and weather:
                print(f"Weather conditions in {weather_data['name']}:")
                print(f"Temperature: {main_data.get('temp')}°C")
                print(f"Weather: {weather.get('main')}")
                print(f"Description: {weather.get('description')}")
            else:
                print("Invalid weather data received. Please try again.")
        else:
            print("Invalid location. Please try again.")
    else:
        print("Unable to retrieve weather data. Please try again.")

def main():
    # location = input("Enter a location: ")
    lat = input("Enter a lat: ")
    long = input("Enter a long: ")
    weather_data = fetch_weather_data(lat, long)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()