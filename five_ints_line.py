#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line


def main():
        counter = 1000
        number = ""
        for counter in range(1000, 2001):
            if (((counter - 1) % 5) == 0):
                #print(counter)
                number += "{}\n ".format(counter)
            else:
                #print(counter)
                number += "{}, ".format(counter)
        print(number)
if __name__ == "__main__":
    main()
