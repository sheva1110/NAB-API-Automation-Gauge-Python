import json
from typing import Any


class JsonUtil:

    @staticmethod
    def load_file(json_file_location: str) -> Any:
        with open(json_file_location, encoding='utf8') as json_file:
            json_data = json.load(json_file)
        return json_data

    @staticmethod
    def format(string: str) -> dict:
        # Format a string to a json dict data type
        return json.loads(string)

    @staticmethod
    def format_json(json_data: str) -> str:
        # Format a string to a json format string
        return json.dumps(json_data, indent=4, ensure_ascii=False)

    @staticmethod
    def convert_dict_to_json(data: dict) -> str:
        return json.dumps(data, ensure_ascii=False)
