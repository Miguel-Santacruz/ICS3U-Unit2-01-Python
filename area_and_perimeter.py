#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: February 2022
# This program calculates area and perimeter of a circle
#   with radius 15mm

import math


def main():
    # This function calculates area and perimeter

    print("If a circle has a radius of 15 mm: ")
    print("")
    print("Its area is {} mm².".format(math.pi * 15**2))
    print("Its perimeter is {} mm.".format(2 * math.pi * 15))

    print("\nDone.")


if __name__ == "__main__":
    main()
