# weather-api

# OpenWeatherMap API Client

A simple and convenient Python client for the OpenWeatherMap API. This package provides easy access to current weather data, forecasts, and other meteorological information.

## Features

- 🌤️ Get current weather by city name
- 🎯 Easy-to-use interface with error handling
- 🔧 Configurable units and language settings
- ⚡ Async support available

## Installation

### From PyPI
```bash
pip install openweather-api
```




## Links
[openweather-api 0.1.1](https://test.pypi.org/project/openweather-api/0.1.1/)


---

# Лабораторная работа
Это лабораторная работа № 3

## Задание

Исследуйте устройство нескольких пакетов, опубликованных на pypi. Например, 
[requests](https://pypi.org/project/requests/)
[yandex-weather-api](https://pypi.org/project/yandex-weather-api/)
[python-open-weather](https://github.com/pmk456/python-open-weather)
Преобразуйте (выполните рефакторинг) вашего существующего проекта для работы с open weather посредством API к виду, возможному для публикации в PyPI.

На основе [инструкции](https://proglib.io/p/kak-opublikovat-svoyu-python-biblioteku-na-pypi-2020-01-28) (или на английском) и рекомендаций статьи [«Разработка идеального pypi пакета с поддержкой разных версий Рython»](https://habr.com/ru/articles/483512/) опубликуйте пакет в [тестовом репозитории пакетов](https://test.pypi.org/). 



В качестве ответа на задание приведите ссылку на ваш пакет в тестовом репозитории пакетов Python, в описании пакета должна быть указана ссылка на репозиторий в гитхаб, где содержится код проекта. 

Постарайтесь приблизиться к описанному в статье «идеальному PyPI-пакету».

## Решение и комментарий

Во время выполнения возникали проблемы с пониманием задания (в процессе эта проблема исчезла). Документация сделана в sphinx

<img width="1045" height="286" alt="image" src="https://github.com/user-attachments/assets/3c41a8b2-7658-422b-a807-604dd7ae4939" />

<img width="1280" height="245" alt="image" src="https://github.com/user-attachments/assets/10f14b43-a413-4d1d-b464-bdfa261deace" />

При выкладывании на TestPyPi возникла проблема с именами пакетов (первое имя существовало и пришлось несколько раз выкладывать и менять версию)

<img width="1800" height="335" alt="image" src="https://github.com/user-attachments/assets/ed79d058-df65-499e-928c-d45075e0bc77" />

<img width="1578" height="249" alt="image" src="https://github.com/user-attachments/assets/ab155964-812e-443f-b756-2254c084e9c9" />


Была еще проблема со скачиванием зависимостей, но эта проблема со стороны TestPyPi (на PyPi их бы не было, распрастраненная проблема)

<img width="1803" height="419" alt="image" src="https://github.com/user-attachments/assets/aba4b3d9-bc15-4511-b32e-e213d0def3e9" />

Но она не влияло на работоспособность (проверка)

<img width="1811" height="396" alt="image" src="https://github.com/user-attachments/assets/40a1de59-a2e1-4b43-bee1-7c16d1642e97" />



