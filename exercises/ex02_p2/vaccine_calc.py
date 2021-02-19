"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730429981"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_to_go: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    exact_date: str = future_date(days_to_go)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% " + "vaccination in " + str(days_to_go) + " days, which falls on ") 
    print(str(exact_date) + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A function evaluating the number of days left until target percent vaccinated is reached."""
    days_to_target = ((population * (target / 100)) - (doses / 2)) / (doses_per_day / 2)
    days_to_target = round(days_to_target)
    return days_to_target


# TODO 3: Define future_date function
def future_date(days_out: int) -> str:
    """A function determining the date the target percent vaccinated is reached."""
    someday: datetime = (datetime.today() + timedelta(days_out))
    return str(someday.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()