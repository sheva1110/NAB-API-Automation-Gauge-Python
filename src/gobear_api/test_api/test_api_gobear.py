from src.gobear_api.api.api_gobear import ApiGoBearList, ApiGoBear
from src.utils import logger
from src.utils.json_util import JsonUtil


class TestGoBear:
    __api_gobear = ApiGoBear()

    def test_basecase(self):
        api = ApiGoBearList.BaseCase
        try:
            response = self.__api_gobear.basecase()
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

    def test_year(self):
        api = ApiGoBearList.Years
        try:
            response = self.__api_gobear.years()
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

    def test_make_year(self, year, car_brand_name: str):
        api = ApiGoBearList.MakeYear
        try:
            response = self.__api_gobear.make_year(year)
            json_data = JsonUtil.format(response.content)

            # TODO: Check response has correct data
            result = response.status_code == 200
            if result:
                # TODO: Log some actual response data
                logger.info(api + ": OK")
                for item in json_data["CarMakes"]:
                    if item["Name"] == car_brand_name:
                        logger.info("Car Brand ID: % s" % item["ID"])
                        return item["ID"]
            else:
                logger.info(api + ": Failed")
                logger.debug(json_data)

        except Exception as ex:
            logger.debug(api, False)
            logger.warning(ex)

    def test_model_year(self, year, car_brand_id: str, model_name: str):
        api = ApiGoBearList.ModelYear % car_brand_id
        try:
            response = self.__api_gobear.model_year(year, car_brand_id)
            json_data = JsonUtil.format(response.content)

            # TODO: Check response has correct data
            result = response.status_code == 200
            if result:
                # TODO: Log some actual response data
                logger.info(api + ": OK")
                for item in json_data["CarModels"]:
                    if item["Name"] == model_name:
                        logger.info("Car model ID: % s" % item["ID"])
                        return item["ID"]
            else:
                logger.info(api + ": Failed")
                logger.debug(json_data)

        except Exception as ex:
            logger.debug(api, False)
            logger.warning(ex)

    def test_variant_year(self, year, car_brand_id: str, car_model_id: str, car_body_type: str):
        api = ApiGoBearList.VariantYear % (car_brand_id, car_model_id)
        try:
            response = self.__api_gobear.variant_year(year, car_brand_id, car_model_id)
            json_data = JsonUtil.format(response.content)

            # TODO: Check response has correct data
            result = response.status_code == 200
            if result:
                # TODO: Log some actual response data
                logger.info(api + ": OK")
                for item in json_data["CarBodyTypes"]:
                    if item["Name"] == car_body_type:
                        logger.info("Car Body Type ID: % s" % item["ID"])
                        return item["ID"]
            else:
                logger.info(api + ": Failed")
                logger.debug(json_data)

        except Exception as ex:
            logger.debug(api, False)
            logger.warning(ex)

    def test_insurance(self, year, car_brand_id: str, car_model_id: str, car_body_type_id: str):
        api = ApiGoBearList.Insurance
        json_data = None
        try:
            response = self.__api_gobear.insurance(year, car_brand_id, car_model_id, car_body_type_id)
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
        return json_data["Insurances"]
