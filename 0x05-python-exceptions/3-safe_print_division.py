#!/usr/bin/python3


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        division = a / b
    except (TypeError, ZeroDivisionError):
        division = None
    finally:
        print("Inside result: {}".format(division))
    return (division)
