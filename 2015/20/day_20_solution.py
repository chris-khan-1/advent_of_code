from functools import reduce


def get_factors(n: int) -> list:
    return set(
        reduce(
            list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)
        )
    )


def get_number_of_presents_for_house(house_number: int) -> int:
    return 10 * sum(get_factors(n=house_number))


def get_lowest_house_number_given_total_presents(total_presents: int) -> int:
    house_number = 1
    present_count = 0
    while present_count < total_presents:
        present_count = get_number_of_presents_for_house(house_number=house_number)
        house_number += 1
    return house_number - 1


def get_new_lowest_house_number_given_total_presents(total_presents: int) -> int:
    house_number = 1
    present_count = 0
    while present_count < total_presents:
        present_count = get_number_of_presents_for_house(house_number=house_number)
        house_number += 1
    return house_number - 1


if __name__ == "__main__":
    input = 33100000
    lowest_house = get_lowest_house_number_given_total_presents(total_presents=input)
    with open("./2015/20/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: The lowest house number is {lowest_house}.\n")
        output_file.write(f"Part 2: ")
