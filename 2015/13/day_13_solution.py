from collections import defaultdict
from itertools import permutations


def parse_information(input: list[str]) -> dict[dict]:
    info_dict = defaultdict(dict)

    for info in input:
        info_list = info.split(" ")
        first_person = info_list[0]
        second_person = info_list[-1].replace(".", "")
        gain_or_lose = info_list[2]
        happiness_change = int(info_list[3])
        if gain_or_lose == "lose":
            happiness_change = -happiness_change
        info_dict[first_person][second_person] = happiness_change
    return info_dict


def add_myself_to_happiness_info(happiness_info: dict[dict]) -> dict[dict]:
    for person in happiness_info.keys():
        happiness_info[person]["Me"] = 0
    happiness_info["Me"] = {person: 0 for person in happiness_info.keys()}
    return happiness_info


def get_pair_happiness(happiness_info: dict, person_1: str, person_2: str) -> int:
    return happiness_info[person_1][person_2] + happiness_info[person_2][person_1]


def get_possible_seating_arrangement(happiness_info: dict) -> list:
    people = set(happiness_info.keys())
    return [list(pair) for pair in permutations(people)]


def get_largest_happiness_change(input: list[str], include_me: bool = False) -> list:
    happiness_info = parse_information(input=input)

    if include_me:
        happiness_info = add_myself_to_happiness_info(happiness_info=happiness_info)
    print
    best_happiness_change = -float("inf")

    seating_arrangements = get_possible_seating_arrangement(
        happiness_info=happiness_info
    )

    for arrangement in seating_arrangements:
        # add first person to end for circle
        arrangement = arrangement + [arrangement[0]]
        happiness_change = 0
        for i in range(len(arrangement) - 1):
            happiness_change += get_pair_happiness(
                happiness_info=happiness_info,
                person_1=arrangement[i],
                person_2=arrangement[i + 1],
            )
        if happiness_change > best_happiness_change:
            best_happiness_change = happiness_change
    return best_happiness_change


if __name__ == "__main__":
    with open("./2015/13/input.txt", "r") as input_file:
        input = [line.strip() for line in input_file.readlines()]
        largest_happiness_change = get_largest_happiness_change(input=input)
        largest_happiness_change_with_me = get_largest_happiness_change(
            input=input, include_me=True
        )
    with open("./2015/13/solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: The largerst happiness change is {largest_happiness_change}.\n"
        )
        output_file.write(
            f"Part 2: The largerst happiness change including myself is {largest_happiness_change_with_me}."
        )
