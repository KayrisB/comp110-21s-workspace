"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730429981"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie():
    x: int = randint(0, 60)
    if x < 30:
        if x < 15:
            return "It's a GREAT day to be a Tar Heel!"
        else: 
            return "Keep pushing--something lovely is on the way!"
    else: 
        if x < 45:
            return "Someone is thankful for your existence."
        else:
            return "You will be the highlight of someone's life someday."

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()