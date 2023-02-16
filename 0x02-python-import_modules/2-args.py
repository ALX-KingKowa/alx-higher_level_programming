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

    for i in range(1, len(sys.argv)):
        print("{}:{}".format(i, sys.argv[i], end='\n'))
