import requests
from typing import Dict, Any, Optional


class WeatherAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()

    def get_weather_by_city(self, city_name: str, units: str = 'metric', lang: str = 'en') -> Optional[Dict[str, Any]]:
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': units,
            'lang': lang
        }

        try:
            response = self.session.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None