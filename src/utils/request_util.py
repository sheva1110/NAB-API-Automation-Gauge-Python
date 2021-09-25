import requests
from requests import Response


class RequestUtil:

    @staticmethod
    def post(url: str, headers: object, data: object) -> Response:
        return requests.post(url, headers=headers, data=data)

    @staticmethod
    def get(url: str, headers: object, params: object) -> Response:
        return requests.get(url, headers=headers, params=params)

    @staticmethod
    def put(url: str, headers: object, data: object) -> Response:
        return requests.put(url, headers, data=data)

    @staticmethod
    def delete(url: str, headers: object, data: object) -> Response:
        return requests.delete(url, headers=headers)
