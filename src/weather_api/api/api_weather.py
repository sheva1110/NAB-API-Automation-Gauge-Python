
from src.utils.string_util import StringUtil
from src.const.const import Const

from src.utils.request_util import RequestUtil



class ApiWeatherList:
    Weather = "/weather"


class ApiWeather:
    __api_key = StringUtil.decrypt(Const.APP_ID) 
    __headers = {}

    def search_weather(self, keyword):
        url = Const.URL + ApiWeatherList.Weather
        params = {
            'q': keyword,
            'appid': self.__api_key
        }
        return RequestUtil.get(url, self.__headers, params)
