#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_args = len(sys.argv) - 1
    print("Number of arguments(s):{}".format(number_args), end='')

    if number_args == 1:
        print("argument", end='')
    elif number_args > 1:
        print('arguments', end='')

    if number_args == 0:
        print(".")
    else:
        print(":")

    for i in range(1, len(sys.argv)):
        print("{}:{}".format(i, sys.argv[i], end='\n'))
