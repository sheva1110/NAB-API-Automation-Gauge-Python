import os
import time
import hashlib
from collections.abc import Mapping
import json

from geopy.geocoders import Nominatim

from src.utils import logger, log_debug


class Common:
    __parent_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    __data_directory = os.path.abspath(os.path.join(__parent_path, os.pardir)) + '/src/data/'

    @staticmethod
    def get_project_root() -> str:
        current_dir = os.path.abspath(os.curdir)
        return str(current_dir.split('src')[0])
