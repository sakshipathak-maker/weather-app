Weather App

1. Project Overview

The Weather App is a command-line Python application that allows a user to enter a city name and retrieve its current weather information.

The application uses Open-Meteo APIs to:

Find the latitude and longitude of the entered city.

Retrieve the current temperature, humidity, and wind speed for that location.

No graphical user interface is required.

2. Features

Accepts a city name from the user.

Dynamically finds the city's coordinates.

Retrieves current weather information.

Displays:

Temperature

Humidity

Wind speed

Handles invalid city names.

Handles API/network connection failures.

Uses functions and dataclasses for better code organization.

Separates API-related logic from the main application flow.

3. Technologies Used

Python

Requests library

Open-Meteo Geocoding API

Open-Meteo Weather API

Python Dataclasses

Virtual Environment

4. Project Structure

weather_app/
│
├── models/
│   └── weather.py
│
├── services/
│   └── weather_service.py
│
├── tests/
│
├── venv/
├── .env
├── main.py
└── requirements.txt

Components

main.py

Handles:

User input

Application flow

Calling service functions

Displaying weather information

services/weather_service.py

Handles:

Communication with the Geocoding API

Communication with the Weather API

Processing API responses

Error handling related to API requests

models/weather.py

Contains dataclasses used to represent application data:

Location

City

Latitude

Longitude

Weather

Temperature

Humidity

Wind speed

tests/

Used for adding automated tests for the application.

.env

Used for environment-specific configuration or secrets when required.

requirements.txt

Contains the Python dependencies required by the project.

5. Application Flow

User enters city
       ↓
main.py
       ↓
get_coordinates()
       ↓
Open-Meteo Geocoding API
       ↓
Location object
(city, latitude, longitude)
       ↓
get_weather()
       ↓
Open-Meteo Weather API
       ↓
Weather object
(temperature, humidity, wind speed)
       ↓
display_weather()
       ↓
Weather displayed to user

6. API Integration

Geocoding API

The Geocoding API converts a city name into geographic coordinates.

City Name
   ↓
Geocoding API
   ↓
Latitude + Longitude

For example:

Mumbai
Latitude: 19.07283
Longitude: 72.88261

Weather API

The latitude and longitude are then passed to the Weather API.

Latitude + Longitude
        ↓
Weather API
        ↓
Temperature
Humidity
Wind Speed

7. Error Handling

The application handles common failures such as:

Invalid City

If the city cannot be found:

Sorry, could not find the city: Mumbhai

Network/API Failure

The application catches request-related exceptions and displays an appropriate error message instead of terminating unexpectedly.

Timeout

API requests use a timeout so the application does not wait indefinitely for a response.

8. How to Run

Step 1: Activate the virtual environment

On Windows:

venv\Scripts\activate

Step 2: Install dependencies

pip install -r requirements.txt

Step 3: Run the application

python main.py

9. Example

Enter City Name (or 'exit' to quit): Mumbai

Fetching weather details for city Mumbai...

Weather in Mumbai
----------------------------
Temperature: 30.5 °C
Humidity: 70 %
Wind Speed: 8.2 km/h

To exit:

Enter City Name (or 'exit' to quit): exit

Thank you for using Weather App!

10. Key Python Concepts Used

The project demonstrates:

Variables and data types

Functions

Function arguments

Conditional statements

Loops

Exception handling

External API integration

JSON response handling

Modules and packages

Dataclasses

Object-oriented concepts

Virtual environments

Separation of responsibilities