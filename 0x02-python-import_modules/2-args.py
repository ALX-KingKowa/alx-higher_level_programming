#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_args = len(sys.argv) - 1

    if number_args == 0:
        print("{} arguments.".format(number_args))
    elif number_args == 1:
        print("{} argument:".format(number_args))
    else:
        print("{} arguments:".format(number_args))

    if number_args >= 1:
        number_args = 0
        for arg in sys.argv:
            if number_args != 0:
                print("{}: {}".format(number_args, arg))
            number_args += 1
