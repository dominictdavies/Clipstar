"""
This module tests all of main.py's functions.
"""

import pytest
from clipstar.main import string_recogniser, main


def test_string_recogniser_string():
    """Tests string_recogniser() with a string input, expects specific phrase"""
    string = "This is a string."
    output = string_recogniser(string)
    assert output == string + " <- That's a string!"


def test_string_recogniser_number():
    """Tests string_recogniser() with a number, expects TypeError"""
    number = 0
    with pytest.raises(TypeError):
        string_recogniser(number)


def test_main(capsys):
    """Tests main(), expects specific terminal outputs"""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello world!\n"
