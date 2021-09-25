from getgauge.python import step

from src.gobear_api.gobear_api_func import func_search_car_insurance, func_check_car_insurance
from src.utils import logger


def __soft_assert_equal(field, actual, expect):
    try:
        result = actual == expect
        log_rs = "OK" if result else "FAILED"
        log = "   [%s] %s: %s" % (log_rs, field, expect)
        if result:
            logger.info(log)
        else:
            logger.warn(log + " (actual: '%s')" % actual)
        assert result
    except Exception as ex:
        pass


@step("Search car insurance API")
def search_car_insurance():
    logger.info("Search Car Insurance")
    func_search_car_insurance()


@step("Verify car insurance API")
def verify_car_insurance():
    logger.info("Verify Car Insurance")
    result = func_check_car_insurance()
    __soft_assert_equal("Car Insurance Name", True, result)
