import itertools
from typing import List, Tuple


def get_starting_grid(size: int) -> List[list]:
    """
    Returns a size x size grid of list of lists.
    Initialised with value 0 signalling off
    """
    return [[0] * size for _ in range(size)]


def extract_instruction(instruction: str) -> Tuple[str, list, list]:
    """
    Extract the command to action and the start and end coordinates of the instruction.
    """
    actions = ["toggle", "turn on", "turn off"]
    for action in actions:
        if action in instruction:
            command = action
            remaining_instruction = (
                instruction.replace(action, "").strip().split(" through ")
            )
            start_coordinate = [int(i) for i in remaining_instruction[0].split(",")]
            end_coordinate = [int(i) for i in remaining_instruction[1].split(",")]
        continue

    return command, start_coordinate, end_coordinate


def turn_on(value):
    return min(value + 1, 1)


def turn_off(value):
    return max(value - 1, 0)


def toggle_light(value):
    toggle_map = {1: 0, 0: 1}
    return toggle_map[value]


def do_instruction(grid: List[list], instruction: str) -> List[list]:
    command, start_coordinate, end_coordinate = extract_instruction(
        instruction=instruction
    )
    x_to_change = [x for x in range(start_coordinate[0], end_coordinate[0] + 1)]
    y_to_change = [y for y in range(start_coordinate[1], end_coordinate[1] + 1)]

    coordinates_to_change = list(itertools.product(x_to_change, y_to_change))

    func_dict = {"turn on": turn_on, "turn off": turn_off, "toggle": toggle_light}

    for coordinate in coordinates_to_change:
        x, y = coordinate
        grid[x][y] = func_dict[command](value=grid[x][y])

    return grid


def do_multiple_instructions(grid: List[list], instructions: List[str]) -> List[list]:
    for instruction in instructions:
        grid = do_instruction(grid=grid, instruction=instruction)
    return grid


if __name__ == "__main__":
    with open("./2015/6/input.txt", "r") as input_file:
        instructions = [line.rstrip() for line in input_file]
        initial_grid = get_starting_grid(1000)
        final_grid = do_multiple_instructions(
            grid=initial_grid, instructions=instructions
        )
        total_lights_on = sum([sum(sublist) for sublist in final_grid])

    with open("./2015/6/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: There are now {total_lights_on} lights on.\n")
