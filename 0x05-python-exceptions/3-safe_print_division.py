#!/usr/bin/python3

def safe_print_division(a, b):
    """divides two integers and prints the result.

    Args:
        a: integer to divide
        b: integer to divide
    Return:
        The value of the division
        Otherwise: None
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
