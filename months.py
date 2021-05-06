#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 06 May 2021
# This program tells the number of days in each month of the year

# Inspired from the website: https://www.faceprep.in/c/program-to-find-
#   the-number-of-days-in-a-given-month-of-a-given-year/

def main():
    # this function tells the number of days in each month of the year

    # input
    month = int(input("Enter the month number (1 - 12): "))
    year = int(input("Enter the year: "))

    # process & output
    if ((month == 1) or (month == 3) or (month == 5) or (month == 7)):
        print("")
        print("This month has 31 days.")

    elif ((month == 8) or (month == 10) or (month == 12)):
        print("")
        print("This month has 31 days.")

    elif ((month == 2) and ((year % 400 == 0))):
        print("")
        print("This month has 29 days this year!")

    elif ((month == 2) and (year % 4 == 0 and year % 100 != 0)):
        print("")
        print("This month has 29 days this year!")

    elif (month == 2):
        print("")
        print("This month has 28 days this year!")

    else:
        print("")
        print("This month has 30 days.")


if __name__ == "__main__":
    main()
