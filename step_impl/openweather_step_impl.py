from src.weather_api.api_func import *
from getgauge.python import step
from src.utils import logger


@step("Search <city> weather API")
def search_weather(city):
    logger.info("Search Weather by city name")
    func_search_weather(city)


@step("Verify <city> in weather response result")
def verify_city(city):
    logger.info("Verify city name in Response")
    func_verify_city_in_weather_result(city)


@step("Verify weather response schema API")
def verify_api_schema():
    logger.info("Verify weather response schema API")
    func_verify_weather_response_schema()

