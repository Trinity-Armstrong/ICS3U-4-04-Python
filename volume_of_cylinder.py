#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program calculates the volume of a cylinder


import math


def calculate(radius, height):
    # This function calculates the volume of a cylinder

    # Process
    volume = (math.pi*radius**2)*height

    return volume


def main():
    # This function gets the radius & height then outputs answer

    # Introduction
    print("We will be calculating the volume of a cylinder in centimeters.")

    # Process
    while True:
        # Input
        user_radius = input("Enter the radius: ")
        user_height = input("Enter the height: ")

        try:
            user_radius = int(user_radius)
            user_height = int(user_height)
            volume = calculate(height=user_height, radius=user_radius)
            if user_radius == int(user_radius) and \
               user_height == int(user_height):
                print("")
                print("The volume of your cylinder is {0}cm³.".format(volume))
                break
            else:
                print("")
                print("Error!")
        except Exception:
            print("")
            print("Error!")
            print("")


if __name__ == "__main__":
    main()
