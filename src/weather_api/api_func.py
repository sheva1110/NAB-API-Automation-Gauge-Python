from src.utils.json_util import JsonUtil
from src.weather_api.api.api_weather import ApiWeather
from src.utils.assert_util import AssertUtil
from src.weather_api import WEATHER_RES_SCHEMA
from getgauge.python import data_store
import jsonschema
from jsonschema import validate

weather_api = ApiWeather()


def func_search_weather(keyword):
    response = weather_api.search_weather(keyword)
    data_store.spec.status_code = response.status_code
    data_store.spec.weather_result = JsonUtil.format(response.content)


def func_verify_weather_status_code(status_code):
    AssertUtil.equal(str(status_code), str(data_store.spec.status_code), "Verify status code")


def func_verify_city_in_weather_result(city):
    AssertUtil.equal(city, data_store.spec.weather_result["name"], "Verify city name is displayed in response body")


def func_verify_country_code_in_weather_result(country):
    AssertUtil.equal(country, data_store.spec.weather_result["sys"]["country"], "Verify country code is displayed in response body")


def func_verify_weather_result_not_display():
    AssertUtil.equal("404", data_store.spec.weather_result["cod"], "Verify weather forecast results are not displayed")
    
  
def __validate_json(json_data):
    try:
        validate(instance=json_data, schema=WEATHER_RES_SCHEMA)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def func_verify_weather_response_schema():
    is_valid = __validate_json(data_store.spec.weather_result)
    AssertUtil.soft_assert_equal("API Schema", is_valid, True)

