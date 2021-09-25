import base64
import copy
import os
import random
import string


class StringUtil:

    @staticmethod
    def convert_phone_no(phone_number: str, is_first_zero_number=False) -> str:
        if is_first_zero_number:
            # Convert a phone number (e.g, '+84589460393') to another format (e.g, '0589460393')
            return '0' + phone_number.lstrip('+84')
        else:
            # Convert a phone number (e.g, '0589460393') to another format (e.g, '+84589460393')
            return '+84' + phone_number.lstrip('0')

    @staticmethod
    def convert_gps_value_to_list(gps_value: str) -> list:
        value = gps_value.split(', ')
        return [value[0], value[1]]

    @staticmethod
    def append_dict(first_dict: dict, second_dict: dict) -> dict:
        cloned_params = copy.deepcopy(first_dict)
        cloned_params.update(second_dict)
        return cloned_params

    @staticmethod
    def encrypt(input_key: str):
        return base64.b64encode(input_key.encode())

    @staticmethod
    def decrypt(input_key):
        return base64.b64decode(input_key).decode('utf-8')

    @staticmethod
    def random_string(size=8):
        # Random a string with size default is 8 - ex: abcdefgx
        lst = [random.choice(string.ascii_letters + string.digits) for _ in range(size)]
        return ''.join(lst)

    @staticmethod
    def random_int(size: int):
        # Random an integer number with a size
        return random.randint(0, size - 1)

    @staticmethod
    def money(money: int):
        # Format an integer to a money string (e.g: 10000 -> '10.000đ')
        currency = "{:0,.0f}đ".format(money)
        return currency.replace(',', '.')

    @staticmethod
    def convert_money_to_int(str_money: str):
        # Format an money string to a integer (e.g: '10.000đ' > 10000, '-15.000đ' > 15000)
        return int(str_money.replace(".", "").replace("₫", "").replace("-", ""))

    @staticmethod
    def join_path(*args):
        return os.path.join(*args)
