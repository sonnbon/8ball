# CS161: HW3 - Magic 8-Ball
# Connor Williams 2021
# This program behaves like a Magic 8-Ball.

# Import all of random to help with randomly
# choosing questions and answers.
# Reviewed random range from Ch. 13 in textbook "Think Python".
# Reviewed random range notes from Video Lectures 6 and 7.
from random import *

# Function prompts user to ask Yes or No question.
# User answers and function outputs a random response.
# Function then asks user whether program should end.
def magic_eight_ball():

    # Assigned a Yes or No input, asking whether to start
    # the program, to ball_shake.
    ball_shake = input("Shake the Magic 8-Ball? Yes (y) or No (n): ")

    # while loop continues with program if 'Yes'.
    # while loop ends the program if user says 'No' or enters nothing.
    # while loop starts over when program is finished executing or if
    # user enters something outside of the Yes or No arguments.
    while True:

        # if/else/elif statement using ball_shake to decide whether to
        # end the program, execute and start over, or just start over.
        if ball_shake.lower() == "yes" or ball_shake.lower() == "y":

            # print extra line for readability
            print('')

            # Assigned random number to prompt_number
            # plus one so zero is not an option, for simplicity.
            prompt_number = randrange(3) + 1

            # Set prompt questions to unique variables
            # for simplicity and readability.
            prompt_one = "What question do you ask of me?\n> "
            prompt_two = "What is it that you want now?\n> "
            prompt_three = "What do you need to know?\n> "

            # if/else/elif statement uses prompt_number to
            # print random prompt.
            if prompt_number == 1:
                input(prompt_one)
            elif prompt_number == 2:
                input(prompt_two)
            else:
                input(prompt_three)

            # Assigned random number to message_number
            # plus one so zero is not an option, for simplicity.
            message_number = randrange(4) + 1

            # Set message answers to unique variables
            # for simplicity and readability.
            message_one = "As I see it, yes.\n"
            message_two = "Most likely not.\n"
            message_three = "Better not tell you now.\n"
            message_four = "Reply hazy, try again later.\n"

            # if/else/elif statement uses message_number to
            # print random Magic 8-Ball message.
            if message_number == 1:
                print(message_one)
            elif message_number == 2:
                print(message_two)
            elif message_number == 3:
                print(message_three)
            else:
                print(message_four)

            # Execute function again to start the program from the top.
            magic_eight_ball()

            # break the while loop to avoid infinite looping.
            break

        # if not 'Yes', then while loop ends the program if user
        # says no or enters nothing.
        elif ball_shake.lower() == "no" or ball_shake.lower() == "n" or ball_shake == "":
            print("Until next time...")

            # break the while loop to avoid infinite looping.
            break

        # If user enters something outside of the initial arguments
        # program will let the user try again and start over.
        else:
            print("Sorry, that's not an answer...\n")

            # re-initialize the ball_shake variable
            ball_shake = input("Shake the Magic 8-Ball? Yes (y) or No (n): ")

magic_eight_ball()