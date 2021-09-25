
from src.weather_api.api.api_weather import ApiWeather, ApiWeatherList
from src.utils import logger
from src.utils.json_util import JsonUtil


class TestWeather:
    __api_weather = ApiWeather()

    def test_api_weather(self, city):
        api = ApiWeatherList.Weather
        try:
            response = self.__api_weather.search_weather(city)
            json_data = JsonUtil.format(response.content)

            # TODO: Check response has correct data
            result = response.status_code == 200

            if result:
                # TODO: Log some actual response data
                logger.info(api + ": OK")
            else:
                logger.info(api + ": Failed")
                logger.debug(json_data)
        except Exception as ex:
            logger.debug(api, False)
            logger.warning(ex)
        return self
