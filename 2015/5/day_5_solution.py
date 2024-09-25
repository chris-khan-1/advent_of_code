def three_vowels_exist(input: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for letter in input:
        if letter in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return True
    return False


def double_letter_exists(input: str) -> bool:
    for position in range(len(input) - 1):
        if input[position] == input[position + 1]:
            return True
    return False


def is_clear_of_bad_strings(input: str) -> bool:
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_string in bad_strings:
        if bad_string in input:
            return False
    return True


def is_nice_string(input: str) -> bool:
    if not is_clear_of_bad_strings(input=input):  # to exit early
        return False
    elif three_vowels_exist(input=input) and double_letter_exists(input=input):
        return True
    return False


if __name__ == "__main__":
    with open("./2015/5/input.txt", "r") as input_file:
        strings = [line.rstrip() for line in input_file]
        total_nice_strings = sum([is_nice_string(input=string) for string in strings])

    with open("./2015/5/solution.txt", "w") as output_file:
        output_file.write(
            f"Part 1: There are a total of {total_nice_strings} nice strings!\n"
        )
