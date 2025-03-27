"""Testing Functions"""
__author__ ="730572910"

import pytest

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_UC1() -> None:
    """Testing invert with single letters"""
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_UC2() -> None:
    """Testing invert with longer strings"""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}

def test_invert_EC1() -> None:
    """Testing invert with duplicate values"""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_count_UC1() -> None:
    """Tests count with a list containing duplicate values."""
    assert count(["pie", "cake", "pie"]) == {"pie": 2, "cake": 1}

def test_count_UC2() -> None:
    """Tests count with all different values."""
    assert count(["cat", "dog", "fish"]) == {"cat": 1, "dog": 1, "fish": 1}

def test_count_EC1() -> None:
    """Tests count with an empty list."""
    assert count([]) == {}


def test_favorite_color_UC1() -> None:
    """Tests favorite_color when everyone likes the same color"""
    assert favorite_color({"Jeanelle": "pink", "Donna": "pink", "Charlie": "pink"}) == "pink"

def test_favorite_color_UC2() -> None:
    """Tests favorite_color when there is a tie, returns first appearing of the colors"""
    assert favorite_color({"Jeanelle": "pink", "Donna": "green", "Charlie": "pink", "Raven": "pink"}) == "pink"

def test_favorite_color_EC1() -> None:
    """Tests favorite_color with an empty dictionary."""
    assert favorite_color({}) == ""


def test_bin_len_UC1() -> None:
    """Tests bin_len with strings and thier length and unqiue values """
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_UC2() -> None:
    """Tests bin_len with  duplicate values"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_EC1() -> None:
    """Tests bin_len with an empty list."""
    assert bin_len([]) == {}