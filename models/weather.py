from dataclasses import dataclass

@dataclass
class Weather:
    temperature: float
    humidity: int
    wind_speed: float

@dataclass
class Location:
    city:str
    latitude: float
    longitude: float