#!/usr/python3
"""
Super-simple Rock–paper–scissors game

"""
import random
hand_symbols = ['rock', 'paper', 'scissor']

def determine_winner(com, human):
    """ Determine winner of the game.

    :param com:   Computer hand
    :param human: Human hand

    :returns void: Nothing is returned.
    """
    print("Computer has", hand_symbols[com], ", you have", hand_symbols[human])
    result = human - com
    if result == 0:
        print("Draw.")
    elif result < 0 or result == 2:
        print("Computer wins.")
    else:
        print("You win.")


if __name__ == "__main__":
    com_hand = random.randint(0, 2)
    print("Type your hand (rock: 0, paper: 1, scissor: 2)")
    human_hand = int(input())
    determine_winner(com_hand, human_hand)
