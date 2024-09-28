import sys
from itertools import groupby

sys.set_int_max_str_digits(1_000_000)


def get_next_look_and_say_number(input: str) -> int:
    groups = ["".join(group) for _, group in groupby(str(input))]
    output = ""
    for group in groups:
        output += str(len(group))  # num of values
        output += group[0]  # value
    return output


def get_final_look_and_say_number(input: int, iterations: int) -> int:
    i = 0
    value = input
    while i < iterations:
        value = get_next_look_and_say_number(input=value)
        i += 1
    return value


if __name__ == "__main__":
    with open("./2015/10/input.txt", "r") as input_file:
        input = str(input_file.read())
        part_one_value = get_final_look_and_say_number(input=input, iterations=40)
        part_one_value_length = len(part_one_value)

        part_two_value = get_final_look_and_say_number(input=input, iterations=50)
        part_two_value_length = len(part_two_value)

    with open("./2015/10/solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: The length of the value after the 40th iteration is {part_one_value_length}.\n"
        )
        output_file.write(
            f"Part 2: The length of the value after the 50th iteration is {part_two_value_length}."
        )
