import argparse
import json 
import os
import io


os.chdir(path="/home/nikita/VScode/gendiff/gendiff")


def read(file):
    with open(file, 'r') as file:
        return json.load(file)


def sort_by(list_to_filter):
    for element in list_to_filter.items():
        for key in element[1]:
            return key


def diff_processing(diff):
    output_buffer = io.StringIO()

    print("{", file=output_buffer)
    for list_element in diff:
        for key, value in list_element.items():
            match key:
                case "minus":
                    print(f"- {value[0]}: {value[1]}", file=output_buffer)
                case "neutral":
                    print(f"  {value[0]}: {value[1]}", file=output_buffer)
                case "plus":
                    print(f"+ {value[0]}: {value[1]}", file=output_buffer)
                case "plus-minus":
                    print(f"- {value[0]}: {value[1]}", file=output_buffer)
                    print(f"+ {value[0]}: {value[1]}", file=output_buffer)
    print("}", file=output_buffer)

    output_string = output_buffer.getvalue()
    return output_string


def gendiff_diff(first_file, second_file):
    result_list = list()

    for key in first_file:
        first = first_file.get(key)
        second = second_file.get(key)
        if first == second:
            result_list.append({"neutral": (key, first)})
        elif first != second and first is not None and second is not None:
            result_list.append({"plus-minus": (key, first)})
        else:
            result_list.append({"minus": (key, first)})

    for key in second_file:
        if key not in first_file:
            result_list.append({"plus": (key, second_file.get(key))})

    result_list.sort(key=sort_by)
    output = diff_processing(result_list)
    return output
    

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    first = read(args.first_file)
    second = read(args.second_file)
    diff = gendiff_diff(first, second)
    print(diff)
