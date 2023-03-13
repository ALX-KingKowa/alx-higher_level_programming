#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): The list of elements to print from.
        x (int): The number of elements to print from my_list.
    Returns:
        The number of elements printed.
    """
    num_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elements += 1
        except IndexError:
            break
    print("")
    return (num_elements)
