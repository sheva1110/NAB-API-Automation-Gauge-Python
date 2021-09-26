from re import S
from src.weather_api.api_func import *
from getgauge.python import step
from src.utils import logger


@step("Search city <city> weather API")
def search_weather(city):
    logger.info("Search Weather by city name")
    func_search_weather(city)

@step("Search city <city> and country code <country> weather API")
def search_weather_city_country(city, country):
    logger.info("Search Weather by city name and country code")
    func_search_weather(city + "," + country)


@step("Verify return status code <status_code>")
def verify_city(status_code):
    logger.info("Verify return status code: " + status_code)
    func_verify_weather_status_code(status_code)


@step("Verify city <city> in weather response result")
def verify_city(city):
    func_verify_city_in_weather_result(city)

@step("Verify country code <country> in weather response result")
def verify_country(country):
    func_verify_country_code_in_weather_result(country)

@step("Verify that weather forecast results are not displayed")
def verify_country():
    logger.info("Verify that weather forecast results are not displayed")
    func_verify_weather_result_not_display()


@step("Verify weather response schema API")
def verify_api_schema():
    func_verify_weather_response_schema()

