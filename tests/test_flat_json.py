import json
from gendiff.cli import gendiff_diff


def read(file):
    with open(file, 'r') as file:
        return json.load(file)


def test_output_first():
    with open("/home/nikita/VScode/gendiff/tests/fixtures/json_files/first.json") as first_json:
        with open ("/home/nikita/VScode/gendiff/tests/fixtures/json_files/second.json") as second_json:
            with open ("/home/nikita/VScode/gendiff/tests/fixtures/output_files/first_second.txt") as output:
                first = json.load(first_json)
                second = json.load(second_json)
                gendiff = gendiff_diff(first, second)
                assert output == gendiff
