from functools import reduce
from itertools import combinations


def get_wrapping_paper_square_footage(dimensions: str) -> int:
    """
    Calculate square footage via formula:
        2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)


    Args:
        dimensions: string of length x width x height (lxwxh).

    Returns:
        Total square footage required.
    """
    dimension_list = [int(i) for i in dimensions.split("x")]
    dimension_combinations = [i for i in combinations(dimension_list, 2)]
    areas = [x * y for x, y in dimension_combinations]
    return (2 * sum(areas)) + min(areas)


def get_ribbon_length(dimensions: str) -> int:
    """
    Get ribbon length via formula:
        2*min(l+w, w+h, h+l) + (l*w*h)


    Args:
        dimensions: string of length x width x height (lxwxh).

    Returns:
        Total ribbon lenght required
    """
    dimension_list = [int(i) for i in dimensions.split("x")]
    dimension_combinations = [i for i in combinations(dimension_list, 2)]
    perimeters = [x + y for x, y in dimension_combinations]
    volume = reduce((lambda x, y: x * y), dimension_list)
    return (2 * min(perimeters)) + volume


if __name__ == "__main__":
    with open("./2015/2/input.txt", "r") as input_file:
        dimensions = [line.rstrip() for line in input_file]
        total_wrapping_paper = sum(
            get_wrapping_paper_square_footage(dimension) for dimension in dimensions
        )
        total_ribbon = sum(get_ribbon_length(dimension) for dimension in dimensions)

    with open("./2015/2/standard_solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: Total wrapping paper needed is {total_wrapping_paper} square foot\n"
        )
        output_file.write(f"Part 2: Total ribbon needed is {total_ribbon} feet")
