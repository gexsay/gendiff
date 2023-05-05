import pytest
import os
import json
from gendiff.cli import gendiff_diff

func_name_length = len("test_output_first")
file_name_length = len(__file__)
file_path = __file__[:file_name_length - func_name_length]


def test_output_first():
    path_first = os.path.abspath(file_path + "fixtures/json_files/first.json")
    path_second = os.path.abspath(file_path + "fixtures/json_files/second.json")
    path_output = os.path.abspath(file_path + "fixtures/output_files/first_second.txt")
    with open(path_first) as first_json:
        with open(path_second) as second_json:
            with open(path_output) as output:
                first = json.load(first_json)
                second = json.load(second_json)
                content = output.read()
                func_output = (gendiff_diff(first, second))
                assert content == func_output


test_output_first()