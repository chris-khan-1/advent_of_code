from itertools import combinations


def get_combinations(containers: list[int], total_size: int) -> list[tuple]:
    container_combinations = []
    for number_of_containers in range(1, len(containers) + 1):
        for combo in combinations(containers, number_of_containers):
            if sum(combo) == total_size:
                container_combinations.append(combo)
    return container_combinations


def get_total_combinations(containers: list[int], total_size: int) -> int:
    return len(get_combinations(containers=containers, total_size=total_size))


def get_min_container_combinations(
    containers: list[int], total_size: int
) -> list[tuple]:
    container_combinations = []
    for number_of_containers in range(1, len(containers) + 1):
        for combo in combinations(containers, number_of_containers):
            if sum(combo) == total_size:
                container_combinations.append(combo)
        if len(container_combinations) == 0:
            container_combinations = []
        else:
            return container_combinations


def get_total_min_container_combinations(containers: list[int], total_size: int) -> int:
    return len(
        get_min_container_combinations(containers=containers, total_size=total_size)
    )


if __name__ == "__main__":
    with open("./2015/17/input.txt", "r") as input_file:
        containers = [int(line) for line in input_file.readlines()]
        total_combos = get_total_combinations(containers=containers, total_size=150)
        total_min_size_combos = get_total_min_container_combinations(
            containers=containers, total_size=150
        )

    with open("./2015/17/solution.txt", "w") as output_file:
        output_file.write(
            (
                "Part 1: The total number of combos to fit 150 litres of eggnog"
                f" is {total_combos}.\n"
            )
        )
        output_file.write(
            (
                "Part 2: The total number of combos, with minimal size, to fit 150"
                f" litres of eggnog is {total_min_size_combos}."
            )
        )
