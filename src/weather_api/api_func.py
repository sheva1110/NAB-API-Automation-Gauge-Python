from src.utils.assert_util import AssertUtil
from src.weather_api import WEATHER_RES_SCHEMA
from src.weather_api.test_api.test_api_weather import TestWeather
from getgauge.python import data_store
from cerberus import Validator

weather_api = TestWeather()


def func_search_weather(city):
    data_store.spec.weather_result = weather_api.test_api_weather(city)


def func_verify_city_in_weather_result(city):
    AssertUtil.equal(city, data_store.spec.weather_result["name"], "Verify city name is displayed in response body")


def func_verify_weather_response_schema():
    validator = Validator(WEATHER_RES_SCHEMA)
    is_valid = validator.validate(data_store.spec.weather_result)
    AssertUtil.soft_assert_equal("API Schema", is_valid, True)

