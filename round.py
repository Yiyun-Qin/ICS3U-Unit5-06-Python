#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, rounding the decimal numbers


def DecimalRound(some_number):
    # This function rounds the decimal

    # process
    number_1 = some_number[0] * pow(10, some_number[1])
    number_2 = number_1 + 0.5
    number_3 = int(number_2)
    some_number[0] = number_3 * pow(10, some_number[1] * -1)


def main():
    # This function does try, catch, input and output
    some_number = []

    # input
    float_string = input("Enter the number you want to round: ")
    decimal_places_string = input(
        "Enter how many decimal places you want to round by: "
    )

    # process & output
    print("")
    try:
        float_enter = float(float_string)
        decimal_places = int(decimal_places_string)
        if decimal_places >= 0:
            some_number.append(float_enter)
            some_number.append(decimal_places)
            # call functions
            DecimalRound(some_number)
            print("The rounded number is {}.".format(some_number[0]))
        else:
            print("Please do not enter negative decimal places!")
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
