def string_recogniser(string):
    if type(string) != str:
        raise TypeError()

    return string + " <- That's a string!"


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
