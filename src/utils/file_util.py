import os
import random
import shutil
from os import path

from src.utils import log_debug
from src.utils.common import Common


class FileUtil:
    __test_case_properties_file_path: str

    @staticmethod
    def create_folder(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    @staticmethod
    def check_file_exist(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def delete_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def read_file(file_path) -> str:
        with open(file_path, 'r', encoding='utf8') as my_file:
            return my_file.read()

    @staticmethod
    def read_properties_file(file_path) -> dict:
        separator = "="
        keys = {}
        with open(file_path, 'r', encoding='utf8') as data:
            for line in data:
                if line[0] == "#":
                    continue
                if separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    keys[name.strip()] = value.strip()
        return keys

    @staticmethod
    def write_properties_file(file_path, key: str, value):
        keys = FileUtil.read_properties_file(file_path)
        with open(file_path, 'w', encoding='utf8') as data:
            for item in keys:
                if item == key:
                    item += '=%s' % str(value) + '\n'
                else:
                    item += '=%s\n' % keys[item]
                data.writelines(item)

    @staticmethod
    def copy_file(src_file_path, des_file_path):
        if path.exists(src_file_path):
            shutil.copy(src_file_path, des_file_path)

    @staticmethod
    def edit_csv_file(csv_path: str, temp_file_path: str, line_num, edit_column: int, edit_data: str,
                      is_random: bool = False):
        # csv_path = src file path
        # temp_file_path = temporary file path. Will be delete after copied
        # line_num = specific line. If all lines, = all
        # edit_column = column has edit data
        # edit data = data need to be edited
        if path.exists(csv_path):
            data = str(FileUtil.read_file(csv_path))  # convert buffer to string
            lines = data.split("\n")  # split string to lines

            file_output = open(temp_file_path, "w", encoding="utf-8")
            file_output.write(lines[0] + "\n")  # write header
            line_number = 1
            while line_number < len(lines) - 1:  # there is a blank line at bottom. So -1 will remove that blank line
                line_data = lines[line_number].split(",")
                if is_random:  # add is_random for inputting random data(if needed) when editing csv file
                    edit_data = ("Random" + str(random.randint(0, 999999999)))
                line_data[edit_column] = edit_data
                # Write file
                col_num = 0
                while col_num < len(line_data):
                    if col_num == (len(line_data) - 1):  # break line at the end of line
                        file_output.write(line_data[col_num] + "\n")
                    else:
                        file_output.write(line_data[col_num] + ",")
                    col_num += 1
                if line_number == line_num:
                    break
                line_number += 1
            file_output.close()
            FileUtil.copy_file(temp_file_path, csv_path)  # copy file
            Common.sleep(5)  # wait for copying file
            FileUtil.delete_file(temp_file_path)  # delete temp file

    @staticmethod
    def edit_csv_file_new(csv_file_path: str, line_num, edit_column: int, edit_data: str, is_random=False):
        if path.exists(csv_file_path):
            data = str(FileUtil.read_file(csv_file_path))  # convert buffer to string
            lines = data.split("\n")  # split string to lines

            file_output = open(csv_file_path, "w", encoding="utf-8")
            file_output.write(lines[0] + "\n")  # write header
            line_number = 1
            while line_number < len(lines) - 1:  # there is a blank line at bottom. So -1 will remove that blank line
                line_data = lines[line_number].split(",")
                if is_random:  # add is_random for inputting random data(if needed) when editing csv file
                    edit_data = ("Random" + str(random.randint(0, 999999999)))
                line_data[edit_column] = edit_data
                # Write file
                col_num = 0
                while col_num < len(line_data):
                    if col_num == (len(line_data) - 1):  # break line at the end of line
                        file_output.write(line_data[col_num] + "\n")
                    else:
                        file_output.write(line_data[col_num] + ",")
                    col_num += 1
                if line_number == line_num:
                    break
                line_number += 1
            file_output.close()

    @staticmethod
    def read_csv_file(csv_path: str, read_column: int, line_num: str = "all"):
        # read csv file and return a array of data, which need to check in CSV file
        # csv_path = src file path
        # line_num = specific line. If all lines, = all
        # read_column = column has selected data
        array_data = []
        if path.exists(csv_path):
            data = str(FileUtil.read_file(csv_path))  # convert buffer to string
            lines = data.split("\n")  # split tring to lines

            line_number = 1
            while line_number < len(lines) - 1:  # there is a blank line at bottom. So -1 will remove that blank line
                line_data = lines[line_number].split(",")
                if line_number == int(line_num):
                    array_data = [line_data[read_column]]
                    break
                array_data.append(line_data[read_column])
                line_number += 1
        return array_data

    @staticmethod
    def read_csv_data(csv_data: str, read_column: int, line_num: str = "all"):
        # csv_data = data after reading csv file
        # line_num = specific line. If all lines, = all
        # read_column = column has selected data
        array_data = []
        data = csv_data
        lines = data.split("\n")  # split tring to lines

        line_number = 1

        if line_num == "all":
            while line_number < len(lines) - 1:  # there is a blank line at bottom. So -1 will remove that blank line
                line_data = lines[line_number].split(",")
                array_data.append(line_data[read_column])
                line_number += 1
        else:
            while line_number < len(lines) - 1:  # there is a blank line at bottom. So -1 will remove that blank line
                line_data = lines[line_number].split(",")
                if line_number == int(line_num):
                    array_data = [line_data[read_column]]
                    break
                array_data.append(line_data[read_column])
                line_number += 1
        return array_data
