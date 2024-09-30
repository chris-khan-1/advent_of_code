import json
import re
from typing import Any


def get_digits_from_string(input: str) -> list[str]:
    """Gets all positive and negative digits from a string"""
    return re.findall(r"[-]?\d+", input)


def get_sum_of_digits_from_string(input: str) -> int:
    digits = get_digits_from_string(input=input)
    return sum([int(i) for i in digits])


def hook(obj: dict[Any, Any]) -> dict[Any, Any]:
    if "red" in obj.values():
        return {}
    return obj


def read_json_no_red(input: str):
    """Read json input with custom hook to remove objects with 'red' in them."""
    return json.loads(s=input, object_hook=hook)


def get_reduced_sum_of_digits_from_json(input: str):
    reduced_input = str(read_json_no_red(input=input))
    return get_sum_of_digits_from_string(input=reduced_input)


if __name__ == "__main__":
    with open("./2015/12/input.json", "r") as input_file:
        input = input_file.read()
        sum_of_all_digits = get_sum_of_digits_from_string(input=input)
        sum_of_reduced_input_digits = get_reduced_sum_of_digits_from_json(input=input)

    with open("./2015/12/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: The sum of all digits is {sum_of_all_digits}.\n")
        output_file.write(
            f"Part 2: The sum of all digits for the reduced input is {sum_of_reduced_input_digits}."
        )
