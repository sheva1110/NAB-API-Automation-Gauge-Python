
from src.const.const import Const
from src.utils.json_util import JsonUtil
from src.utils.request_util import RequestUtil


class ApiWeatherList:
    Weather = "/weather"


class ApiWeather:
    __headers = {}

    def search_weather(self, city):
        url = Const.URL + ApiWeatherList.Weather
        params = {
            'q': city,
            'appid': Const.APP_ID
        }
        return RequestUtil.get(url, self.__headers, params)
