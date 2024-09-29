from string import ascii_lowercase


def next_letter(old_letter: str) -> str:
    if old_letter == "z":
        return "a"
    return ascii_lowercase[ascii_lowercase.index(old_letter) + 1]


def update_password_with_next_letter(
    old_password: str, letter: str, letter_index: int
) -> str:
    return (
        old_password[:letter_index]
        + next_letter(old_letter=letter)
        + old_password[letter_index + 1 :]
    )


def get_next_possible_password(old_password: str) -> str:
    new_password = old_password
    for i, letter in enumerate(old_password[::-1]):
        letter_index = len((old_password)) - i - 1  # to get acutal letter index
        if letter == "z":
            new_password = update_password_with_next_letter(
                new_password, letter, letter_index
            )
            continue  # continue onto changing next letter
        # update the final letter that is not z
        return update_password_with_next_letter(new_password, letter, letter_index)


def three_letter_straight_exists(password: str) -> bool:
    alphabet = ascii_lowercase
    increasing_three_letters = [
        "".join([alphabet[i], alphabet[i + 1], alphabet[i + 2]]) for i in range(26 - 2)
    ]

    for triple in increasing_three_letters:
        if triple in password:
            return True
    return False


def has_valid_letters(password: str) -> bool:
    for invalid_letter in ["i", "o", "l"]:
        if invalid_letter in password:
            return False
    return True


def has_pair_letters(password: str) -> bool:
    alphabet = ascii_lowercase
    pair_count = 0
    for letter in alphabet:
        if letter * 2 in password:
            pair_count += 1
        if pair_count == 2:
            return True
    return False


def is_password_valid(password: str) -> bool:
    # assume input is already eight characters
    if (
        three_letter_straight_exists(password=password)
        and has_valid_letters(password=password)
        and has_pair_letters(password=password)
    ):
        return True

    return False


def get_next_valid_password(old_password: str, is_valid: bool = False) -> str:
    new_password = old_password
    while is_valid is False:
        new_password = get_next_possible_password(old_password=new_password)
        is_valid = is_password_valid(password=new_password)
    return new_password


if __name__ == "__main__":
    with open("./2015/11/input.txt", "r") as input_file:
        old_password = input_file.read()
        next_valid_password = get_next_valid_password(old_password=old_password)
        next_next_valid_password = get_next_valid_password(
            old_password=next_valid_password
        )

    with open("./2015/11/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: The next valid password is {next_valid_password}\n")
        output_file.write(
            f"Part 2: The next valid password is {next_next_valid_password}"
        )
