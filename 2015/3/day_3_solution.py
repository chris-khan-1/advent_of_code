from collections.abc import Generator


def get_next_house_cordinate(
    start_coordinates: tuple, direction: str
) -> tuple[int, int]:
    x, y = start_coordinates
    if direction == "^":
        y += 1
    if direction == ">":
        x += 1
    if direction == "v":
        y -= 1
    if direction == "<":
        x -= 1
    return (x, y)


def get_all_house_visit_coordinates(directions: str) -> list[tuple[int, int]]:
    house_coordinates = [(0, 0)]
    start_coordinates = (0, 0)
    for direction in directions:
        next_visit_coordinates = get_next_house_cordinate(
            start_coordinates=start_coordinates, direction=direction
        )
        house_coordinates.append(next_visit_coordinates)
        start_coordinates = next_visit_coordinates
    return house_coordinates


def get_total_unique_house_visits(directions: str) -> int:
    unique_houses = set(get_all_house_visit_coordinates(directions=directions))
    return len(unique_houses)


def split_directions(directions: str) -> tuple:
    santa_directions = directions[::2]
    robo_santa_directions = directions[1::2]
    return santa_directions, robo_santa_directions


def get_new_total_unique_house_visits(directions: str) -> int:
    """Gets the total unique house visits with Robo-Santa included"""
    santa_directions, robo_santa_directions = split_directions(directions=directions)
    santa_unique_houses = set(
        get_all_house_visit_coordinates(directions=santa_directions)
    )
    robo_santa_unique_houses = set(
        get_all_house_visit_coordinates(directions=robo_santa_directions)
    )
    return len(santa_unique_houses.union(robo_santa_unique_houses))


if __name__ == "__main__":
    with open("./2015/3/input.txt", "r") as input_file:
        direction_string = input_file.read()
        total_unique_house_visits = get_total_unique_house_visits(
            directions=direction_string
        )
        new_total_unique_house_visits = get_new_total_unique_house_visits(
            directions=direction_string
        )

    with open("./2015/3/solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: Number of houses with at least one present is {total_unique_house_visits}\n"
        )
        output_file.write(
            f"Part 2: With the addition of Robo-Santa, {new_total_unique_house_visits} got presents"
        )
