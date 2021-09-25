from getgauge.python import data_store

from src.gobear_api.test_api.test_api_gobear import TestGoBear
from src.obj.data_info_input import DataInfoInput

gobear_api = TestGoBear()


def func_search_car_insurance():
    data: DataInfoInput = data_store.spec.data_input
    gobear_api.test_basecase()
    gobear_api.test_year()
    car_brand_id = gobear_api.test_make_year(data.car_year, data.car_brand_name)
    car_model_id = gobear_api.test_model_year(data.car_year, car_brand_id, data.car_model_name)
    car_body_type_id = gobear_api.test_variant_year(data.car_year, car_brand_id, car_model_id,
                                                    data.car_body_type_name)
    car_insurrance_collection = gobear_api.test_insurance(data.car_year, car_brand_id, car_model_id,
                                                          car_body_type_id)
    data_store.spec.car_insurance_collection = car_insurrance_collection


def func_check_car_insurance():
    data: DataInfoInput = data_store.spec.data_input
    for item in data_store.spec.car_insurance_collection:
        if item["InsurerName"] == data.car_insurance_expect:
            return True
    return False
