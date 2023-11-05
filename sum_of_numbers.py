#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 15, 2023
# This program will ask the user
# for a integer and it will tell them the sum
# of all the numbers added to it with try catch


def main():
    # initialize counter and sum variables
    sum = 0
    counter = 0

    # Get the user number as a string and display message about program
    print("This program will ask the user for a integer and it will tell them the sum")
    print("of all the numbers added to it.")
    user_number_as_string = input("Please enter a positive integer: ")

    # Catch if the user number is something wrong
    try:
        # Convert user number as a string to int
        user_number_as_int = int(user_number_as_string)

        if counter > user_number_as_int:
            # Message for negative user number
            print("\n{} is not a positive int.".format(user_number_as_string))

        # loop for sum of user_number_as_int
        else:
            while counter <= user_number_as_int:
                # calculate sum
                sum = sum + counter

                # increment counter
                counter = counter + 1

                # display sum to user and counter to user
                print("The loop ran {}".format(counter))

            # display sum to user and counter to user
            print(
                "\nThe sum of the number from 0 to {0} = {1}".format(
                    user_number_as_int, sum
                )
            )

    # Display a message to the user if they entered something that is not valid
    except Exception:
        # Message for invalid user number
        print("\n{} is not a valid int.".format(user_number_as_string))


if __name__ == "__main__":
    main()
