from src.utils import log_debug, logger


def verify_equal(expect, actual, message):
    result = expect == actual
    log = "   %s: %s" % (message, result)
    expect_log = "      Expect: %s" % expect
    actual_log = "      Actual: %s" % actual
    if result:
        log_debug(log)
    else:
        log = log + "\n"
        log += "\t\t\t   " + expect_log + "\n"
        log += "\t\t\t   " + actual_log
        logger.warning(log)
    assert result
