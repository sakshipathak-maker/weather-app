from models.weather import Weather,Location
import requests
#Step 1 : Find the city coordinates
def get_coordinates(city):

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    params={
        "name" : city,
        "count" : 1
    }

    try:
        response = requests.get(geocoding_url, params=params,timeout=10)
    except requests.exceptions.RequestException as e:
        print("Error while connecting to weather service : ", e)
        return None

    print(response.status_code)
    data = response.json()
    print(data)

    if "results" not in data or not data["results"] :
        print(f"Sorry Could Not Find The City: {city}")
        return None
    
    

    location = data["results"][0]

    return Location(
        city=location["name"],
        latitude=location["latitude"],
        longitude=location["longitude"]
    )
       

#Get weather
def get_weather(latitude,longitude):


    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude" : latitude,
        "longitude": longitude,
        "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    try:

        weather_response = requests.get(weather_url,params=weather_params,timeout=10)
    except requests.exceptions.RequestException as e:
        print("Error while connecting to the weather service :" , e)
        return None

    print("Weather API Status:", weather_response.status_code)
    weather_data = weather_response.json()

    current = weather_data["current"]
    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]
    return Weather(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed
    )