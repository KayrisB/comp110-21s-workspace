"""Tar Heels exercise redux as a structured program."""

__author__ = "730429981"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(choice: int) -> str:
    """A small logic puzzle, full of school spirit."""
    if choice % 2 == 0 and choice % 7 == 0:
        return str("TAR HEELS")
    if choice % 2 == 0 or choice % 7 == 0: 
        if choice % 7: 
            return str("TAR")
        if choice % 2:
            return str("HEELS")
    else:
        return str("CAROLINA")
    return "CAROLINA"


if __name__ == "__main__":
    main()