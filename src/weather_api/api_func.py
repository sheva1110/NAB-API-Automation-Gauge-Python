from src.weather_api.test_api.test_api_weather import TestWeather
from getgauge.python import data_store
from src.obj.data_info_input import DataInfoInput

weather_api = TestWeather()


def func_search_weather():
    data: DataInfoInput = data_store.spec.data_input
    data_store.spec.weather_result = weather_api.test_api_weather(data.city)


def func_check_weather_result():
    data: DataInfoInput = data_store.spec.data_input
    
