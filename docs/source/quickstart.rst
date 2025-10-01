Quick Start
===========

.. code-block:: python

   from weather_api import WeatherAPI

   client = WeatherAPI(api_key="your_api_key")
   weather = client.get_weather_by_city("London")

   if weather:
       print(f"Temperature: {weather['main']['temp']}°C")