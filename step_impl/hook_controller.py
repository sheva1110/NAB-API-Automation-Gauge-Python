from src.const.const import Const
from getgauge.python import data_store, ExecutionContext, before_suite, before_spec, \
    before_scenario, before_step, after_spec, after_suite, after_step
from src.obj.data_info_input import DataInfoInput
from src.utils.file_util import FileUtil


# ---------------
# Execution Hooks
# ---------------


@before_suite
def before_suite_hook():
    config = FileUtil.read_properties_file(Const.CONFIG_FILE)

    # Add Gauge suite variables
    data_store.suite.is_debug = config["debug"]


@before_spec()
def before_spec_hook(context: ExecutionContext):
    pass


@before_scenario()
def before_scenario_hook():
    pass


@before_step
def before_step_hook():
    pass


@after_step()
def after_step_hook(context: ExecutionContext):
    pass


# @after_scenario()
# def after_scenario_hook(context: ExecutionContext):
#     pass


@after_spec()
def after_spec_hook(context: ExecutionContext):
    pass


@after_suite()
def after_suite_hook(context: ExecutionContext):
    pass
