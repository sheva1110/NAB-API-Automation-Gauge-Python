from src.utils.assert_util import AssertUtil
from src.weather_api import WEATHER_RES_SCHEMA
from src.weather_api.test_api.test_api_weather import TestWeather
from getgauge.python import data_store
import jsonschema
from jsonschema import validate

weather_api = TestWeather()


def func_search_weather(city):
    data_store.spec.weather_result = weather_api.test_api_weather(city)


def func_verify_city_in_weather_result(city):
    AssertUtil.equal(city, data_store.spec.weather_result["name"], "Verify city name is displayed in response body")
    
    
def __validate_json(json_data):
    try:
        validate(instance=json_data, schema=WEATHER_RES_SCHEMA)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def func_verify_weather_response_schema():
    is_valid = __validate_json(data_store.spec.weather_result)
    AssertUtil.soft_assert_equal("API Schema", is_valid, True)

