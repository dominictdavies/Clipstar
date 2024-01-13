from clipstar.main import *
import pytest


def test_string_recogniser_string():
    string = "This is a string."
    output = string_recogniser(string)
    assert output == string + " <- That's a string!"


def test_string_recogniser_number():
    number = 0
    with pytest.raises(TypeError):
        string_recogniser(number)


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello world!\n"
