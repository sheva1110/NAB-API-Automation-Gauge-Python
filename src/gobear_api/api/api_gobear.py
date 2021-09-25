from src.consts.consts import Consts
from src.utils.json_util import JsonUtil
from src.utils.request_util import RequestUtil


class ApiGoBearList:
    BaseCase = "/api/cars/basecases"
    Years = "/api/cars/years"
    MakeYear = "/api/cars/makes"
    ModelYear = "/api/cars/makes/%s/models"
    VariantYear = "/api/cars/makes/%s/models/%s/varients"
    Insurance = "/api/cars/insurances"


class ApiGoBear:
    __headers = {
        "content-type": "application/json"
    }

    def basecase(self):
        url = Consts.URL + ApiGoBearList.BaseCase
        params = {
        }
        return RequestUtil.get(url, self.__headers, params)

    def years(self):
        url = Consts.URL + ApiGoBearList.Years
        params = {
        }
        return RequestUtil.get(url, self.__headers, params)

    def make_year(self, year):
        url = Consts.URL + ApiGoBearList.MakeYear
        params = {
            "year": year
        }
        return RequestUtil.get(url, self.__headers, params)

    def model_year(self, year, car_brand_id):
        url = Consts.URL + ApiGoBearList.ModelYear % car_brand_id
        params = {
            "year": year
        }
        return RequestUtil.get(url, self.__headers, params)

    def variant_year(self, year, car_brand_id: str, car_model_id: str):
        url = Consts.URL + ApiGoBearList.VariantYear % (car_brand_id, car_model_id)
        params = {
            "year": year
        }
        return RequestUtil.get(url, self.__headers, params)

    def insurance(self, year, car_brand_id, car_model_id, car_body_type_id):
        url = Consts.URL + ApiGoBearList.Insurance
        params = {
            "carYear": year,
            "carMakeId": car_brand_id,
            "carModelId": car_model_id,
            "carBodyTypeId": car_body_type_id,
            "isPrivateUsage": True,
            "isStillPaying": True,
            "sumInsured": 455000,
            "fmv": 455000,
            "requestAon": True,
            "requestPa": False,
            "requestRa": False,
            "classification": 1,
            "CoverageValue_VTPL": 200000
        }
        return RequestUtil.get(url, self.__headers, params)
