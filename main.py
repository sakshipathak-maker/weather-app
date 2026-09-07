""" city = input("Enter City Name = ")
print(f"Fetching weather for city = {city}...")
"""
"""
# IT WILL GIVE OUTPUT FOR AHEMDABAD ONLY AS WE HAVE SET ITS LATITUDE AND LONGITUDE
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 23.0225,
    "longitude": 72.5714,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)

print(response.status_code)
data = response.json()
current = data["current"]
temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind_speed= current["wind_speed_10m"]

print("Temperature:", temperature , "degree celcius")
print("Humidity : ",humidity , "%")
print("wind_speed " ,wind_speed , "km/h")

"""

#Now we want any city's latitude and logitude that user enters  and then connect to weather api and display weather 
#for this we will use Open Meteo's Geocoding API
from services.weather_service import get_coordinates, get_weather
import requests


#step 3 : Display Result
 #Display
def display_weather(location,weather):
    print()
    print("Weather in ", location.city)
    print("----------------------------")
    print("Temperature : ",weather.temperature ,"degree celcius")
    print("Humidity : ", weather.humidity ,"%")
    print("wind speed : ",weather.wind_speed , "km/h")

def main():

    while True:

        city = input("\nEnter City Name (or 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank You for using weather app!")
            break

        if not city:
            print("City Name Can Not be Empty")
            continue
        
        print(f"Fetching weather details for city {city}...")     
        #Get Coordinates
        location = get_coordinates(city)   

        if location is None:
            continue

        #get weather using coordinates
        weather = get_weather(
            location.latitude,
            location.longitude
        )
        #Display Weather
        display_weather(location,weather)
       
if __name__=="__main__":
    main()