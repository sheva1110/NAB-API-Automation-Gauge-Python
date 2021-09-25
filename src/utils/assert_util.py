from src.utils import logger, log_debug


class AssertUtil:
    @staticmethod
    def true(expected_value: bool, log: str = None):
        log = "  %s is True" % log
        result = expected_value
        if result:
            log_debug("%s: %s" % (log, result))
        else:
            logger.warning("%s: %s\n"
                           "\t\t\t\t   Expect: True\n"
                           "\t\t\t\t   Actual: False" % (log, result))
        assert result

    @staticmethod
    def equal(expected_value: str, actual_value: str, log_step_name: str = None):
        log = "  %s is '%s'" % (log_step_name, expected_value)
        result = expected_value == actual_value
        if result:
            log_debug("%s: %s" % (log, result))
        else:
            logger.warning("%s: %s\n"
                           "\t\t\t\t   Expect: '%s'\n"
                           "\t\t\t\t   Actual: '%s'" % (log, result, expected_value, actual_value))
        assert result

    @staticmethod
    def equal_or_lower(expected_value: str, actual_value: str, log_step_name: str = None):
        log = "  %s is lower or equal '%s'" % (log_step_name, expected_value)
        result = int(actual_value) <= int(expected_value)
        if result:
            log_debug("%s: %s" % (log, result))
        else:
            logger.warning("%s: %s\n"
                           "\t\t\t\t   Expect: '%s'\n"
                           "\t\t\t\t   Actual: '%s'" % (log, result, expected_value, actual_value))
        assert result

    @staticmethod
    def not_equal(expected_value: str, actual_value: str, log_step_name: str = None):
        log = "  %s is not '%s'" % (log_step_name, expected_value)
        result = expected_value != actual_value
        if result:
            log_debug("%s: %s" % (log, result))
        else:
            logger.warning("%s: %s\n"
                           "\t\t\t\t   Expect: '%s'\n"
                           "\t\t\t\t   Actual: '%s'" % (log, result, expected_value, actual_value))
        assert result

    @staticmethod
    def contain(expected_value: str, actual_value: str, log_step_name: str = None):
        log = "  %s is '%s'" % (log_step_name, expected_value)
        result = expected_value in actual_value
        if result:
            log_debug("%s: %s" % (log, result))
        else:
            logger.warning("%s: %s\n"
                           "\t\t\t\t   Expect: '%s'\n"
                           "\t\t\t\t   Actual: '%s'" % (log, result, expected_value, actual_value))
        assert result

    @staticmethod
    def soft_assert_equal(field, actual, expect):
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
