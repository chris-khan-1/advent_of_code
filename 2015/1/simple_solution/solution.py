def get_direction(input: str):
    """
    Gets direction or up (+1) or down (-1) a floor

    Args:
        input: string consisting of '(' or ')'.

    Returns:
        Value for direction
    """
    if input == "(":
        return 1
    elif input == ")":
        return -1


def get_final_floor(input: str) -> int:
    """
    Retrieves the final floor.

    Args:
        input: string consisting of '(' and ')'.

    Returns:
        The final floor value.
    """
    floor = 0
    for i in input:
        floor += get_direction(input=i)
    return floor


def get_basement(input: str) -> int:
    """
    Gets the character position when you reach the basement.

    Args:
        input: string consisting of multiple '(' and/or ')'.

    Returns:
        Character position of basement
    """
    floor = 0
    for character_position, character in enumerate(input):
        floor += get_direction(input=character)

        if floor == -1:
            return character_position + 1

    return "Basement was not reached"


# Another solution
# def get_final_floor(input: str) -> int:
#     mapping = {"(": 1, ")": -1}

#     return sum([mapping[i] for i in list(input)])

if __name__ == "__main__":
    with open("./2015/1/input.txt", "r") as input_file:
        string_input = input_file.read()
        final_floor = get_final_floor(input=string_input)
        basement_character_position = get_basement(input=string_input)

    with open("./2015/1/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: Santa ends up on floor {final_floor}\n")
        output_file.write(
            f"Part 2: Character position for basement is {basement_character_position}"
        )
