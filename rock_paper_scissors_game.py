#!/usr/bin/python3

'''Implimenting rock paper scissors game'''
import random


def computer_choice():
    '''Returns the number the computer selected'''
    rand_num = random.randint(1, 3)  # getting random number from 1 to 3
    choices = {1: "rock", 2: "paper", 3: "scissors"}  #dict to select from
    computer_choice = choices[rand_num]
    return computer_choice

def user_input():
    '''Returns the input from the user'''
    user_input = input("Enter rock, paper or scissors: ")
    user_input = user_input.lower()  #capitalize user input first letter
    return user_input

def game_outcome(user_selection, computer_selection):
    '''Returns draw, win or lose

    Args:
        user_selection (str): The user selection
        computer_selection (int): The computer selction at random

    Returns:
        Draw if user makes the same choice with the computer
        Win if user makes superior choice than the computer
        Lose if user makes inferior choice than the computer

    '''
    if computer_selection == user_selection:
        return "draw"
    elif user_selection == "paper" and computer_selection == "rock":
        return "win"
    elif user_selection == "scissors" and computer_selection == "paper":
        return "win"
    elif user_selection == "rock" and computer_selection == "scissors":
        return "win"
    elif user_selection == "scissors" and computer_selection == "rock":
        return "lose"
    elif user_selection == "paper" and computer_selection == "scissors":
        return "lose"
    elif user_selection == "rock" and computer_selection == "paper":
        return "lose"
    else:
        return "Invalid Input.\n You Lose"

if __name__ == "__main__":
    computer_selection = computer_choice()
    user_selection = user_input()
    outcome = game_outcome(user_selection, computer_selection)

    print("Computer's selection: {}".format(computer_selection))
    print("Your pick: {}".format(user_selection))
    print("{}".format(outcome))
