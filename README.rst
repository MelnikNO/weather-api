Open Weather API
================

A simple and convenient Python client for the OpenWeatherMap API.

Installation
------------

.. code-block:: bash

   pip install openweather_api

Quick Start
-----------

.. code-block:: python

   from open_weather_api import WeatherAPI

   # Initialize the client with your API key
   client = WeatherAPI(api_key="YOUR_API_KEY")

   # Get weather for a city
   weather_data = client.get_weather_by_city("London", lang='en')

   if weather_data:
       print(f"Weather in {weather_data['name']}:")
       print(f"Temperature: {weather_data['main']['temp']}°C")
       print(f"Description: {weather_data['weather'][0]['description']}")
   else:
       print("Failed to get weather data.")

Features
--------

- Get current weather by city name
- Support for metric, imperial, and standard units
- Multiple language support
- Simple and intuitive API

Available Methods
-----------------

- ``get_weather_by_city(city_name, units='metric', lang='en')`` - Get weather by city name
- *Add more methods as you develop them*

Parameters
----------

- ``city_name``: Name of the city (e.g., 'London', 'New York')
- ``units``: Temperature units ('metric', 'imperial', 'standard')
- ``lang``: Response language ('en', 'ru', 'fr', 'de', etc.)

Example with Different Parameters
---------------------------------

.. code-block:: python

   # Get weather in Fahrenheit for New York
   weather = client.get_weather_by_city("New York", units='imperial')

   # Get weather in Russian for Moscow
   weather = client.get_weather_by_city("Moscow", lang='ru')

Links
-----

- `Source Code on GitHub <https://github.com/MelnikNO/weather-api>`_
- `OpenWeatherMap API Documentation <https://openweathermap.org/api>`_


