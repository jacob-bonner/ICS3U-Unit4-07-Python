#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program outputs all integers between 1000 - 2000


def main():
    # This program outputs all integers between 1000 - 2000

    # Process
    for counter in range(1000, 2001):
        print(counter, end=" ")
        if counter % 5 == 4:
            print(" ")


if __name__ == "__main__":
    main()
