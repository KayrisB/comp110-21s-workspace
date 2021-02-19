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
    print("We will reach " + str(target) + "% " + "vaccination in " + str(days_to_go) + " days, which falls on " + str(exact_date) + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    days_to_target = ((population * (target / 100)) - (doses / 2)) / (doses_per_day / 2)
    round(days_to_target)
    return int(days_to_target)


# TODO 3: Define future_date function
def future_date(days_out: int) -> str:
    someday: datetime = (datetime.today() + timedelta(days_out))
    return str(someday.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()