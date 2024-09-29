from dataclasses import dataclass
from itertools import combinations


@dataclass
class Cuboid:
    length: int
    width: int
    height: int

    @property
    def dimension_combinations(self) -> list:
        return [i for i in combinations([self.length, self.width, self.height], 2)]

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    @property
    def surface_areas(self) -> list:
        return [x * y for x, y in self.dimension_combinations]

    @property
    def perimeters(self) -> list:
        return [2 * (x + y) for x, y in self.dimension_combinations]


def get_wrapping_paper_square_footage(dimensions: str) -> int:
    """
    Calculate square footage via formula:
        2*(sum of surface areas) + min(surface areas)


    Args:
        dimensions: string of length x width x height (lxwxh).

    Returns:
        Total square footage required.
    """
    dimension_list = [int(i) for i in dimensions.split("x")]
    present_shape = Cuboid(*dimension_list)
    return (2 * sum(present_shape.surface_areas)) + min(present_shape.surface_areas)


def get_ribbon_length(dimensions: str) -> int:
    """
    Get ribbon length via formula:
        min(perimeters) + volume


    Args:
        dimensions: string of length x width x height (lxwxh).

    Returns:
        Total ribbon lenght required
    """
    dimension_list = [int(i) for i in dimensions.split("x")]
    present_shape = Cuboid(*dimension_list)
    return (min(present_shape.perimeters)) + present_shape.volume


if __name__ == "__main__":
    with open("./2015/2/input.txt", "r") as input_file:
        dimensions = [line.rstrip() for line in input_file]
        total_wrapping_paper = sum(
            get_wrapping_paper_square_footage(dimension) for dimension in dimensions
        )
        total_ribbon = sum(get_ribbon_length(dimension) for dimension in dimensions)

    with open("./2015/2/class_solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: Total wrapping paper needed is {total_wrapping_paper} square foot\n"
        )
        output_file.write(f"Part 2: Total ribbon needed is {total_ribbon} feet")
