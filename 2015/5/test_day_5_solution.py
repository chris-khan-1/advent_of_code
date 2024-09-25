import pytest
from day_5_solution import (
    double_letter_exists,
    is_clear_of_bad_strings,
    is_nice_string,
    three_vowels_exist,
)


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("aaa", True),
        pytest.param("eee", True),
        pytest.param("iii", True),
        pytest.param("ooo", True),
        pytest.param("uuu", True),
        pytest.param("xyz", False),
    ],
)
def test_three_vowels_exist(input, expected):
    actual = three_vowels_exist(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[pytest.param("aa", True), pytest.param("xy", False)],
)
def test_double_letter_exists(input, expected):
    actual = double_letter_exists(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("ab", False),
        pytest.param("cd", False),
        pytest.param("pq", False),
        pytest.param("xy", False),
        pytest.param("aa", True),
    ],
)
def test_is_clear_of_bad_strings(input, expected):
    actual = is_clear_of_bad_strings(input=input)
    assert actual == expected


@pytest.mark.parametrize(
    argnames=["input", "expected"],
    argvalues=[
        pytest.param("ugknbfddgicrmopn", True),
        pytest.param("aaa", True),
        pytest.param("jchzalrnumimnmhp", False),
        pytest.param("haegwjzuvuyypxyu", False),
        pytest.param("dvszwmarrgswjxmb", False),
    ],
)
def test_is_nice_string(input, expected):
    actual = is_nice_string(input=input)
    assert actual == expected
