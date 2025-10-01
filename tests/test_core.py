import unittest
from unittest.mock import Mock, patch
import sys
import os
import importlib.util

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

spec = importlib.util.spec_from_file_location(
    "weather_api",
    os.path.join(os.path.dirname(__file__), '../src/weather_api/__init__.py')
)
weather_api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weather_api)
WeatherAPI = weather_api.WeatherAPI


class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        self.api_key = "test_api_key"
        self.weather_api = WeatherAPI(api_key=self.api_key)

    def test_initialization(self):
        self.assertEqual(self.weather_api.api_key, self.api_key)
        self.assertIsNotNone(self.weather_api.session)

    @patch('weather_api.core.requests.Session.get')
    def test_get_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "main": {"temp": 15.5},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response

        result = self.weather_api.get_weather_by_city("London")

        self.assertEqual(result["name"], "London")
        self.assertEqual(result["main"]["temp"], 15.5)

        mock_get.assert_called_once()
        call_args = mock_get.call_args[1]['params']
        self.assertEqual(call_args['q'], "London")
        self.assertEqual(call_args['appid'], self.api_key)

    @patch('weather_api.core.requests.Session.get')
    def test_get_weather_custom_params(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "Moscow"}
        mock_get.return_value = mock_response

        result = self.weather_api.get_weather_by_city("Moscow", units='imperial', lang='ru')

        self.assertIsNotNone(result)
        call_args = mock_get.call_args[1]['params']
        self.assertEqual(call_args['units'], 'imperial')
        self.assertEqual(call_args['lang'], 'ru')


if __name__ == '__main__':
    unittest.main()