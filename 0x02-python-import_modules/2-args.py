#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments"""

    import sys
    num = len(sys.argv)
    if num == 0:
        print("{} arguments.".format(num - 1))
    elif num == 1:
        print("{} arguments:".format(num-1))
    else:
        print("{} arguments:".format(num-1))

    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))
