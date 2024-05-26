"""
Overloading Special Methods.py
author:张辰旭
date:2023.5.9
description:Overloading Special Methods
"""
import random
class Rock:
    def __lt__(self, other):
        return isinstance(other, Paper)

    def __gt__(self, other):
        return isinstance(other, Scissors)

    def __eq__(self, other):
        return isinstance(other, Rock)

    def str(self):
        return "Rock"


class Scissors:
    def __lt__(self, other):
        return isinstance(other, Rock)

    def __gt__(self, other):
        return isinstance(other, Paper)

    def __eq__(self, other):
        return isinstance(other, Scissors)

    def str(self):
        return "Scissors"


class Paper:
    def __lt__(self, other):
        return isinstance(other, Scissors)

    def __gt__(self, other):
        return isinstance(other, Rock)

    def __eq__(self, other):
        return isinstance(other, Paper)

    def str(self):
        return "Paper"


class Player:
    def play(self):
        options = [Rock(), Paper(), Scissors()]
        return random.choice(options)

class HumanPlayer:
    def play(self):
        while True:
            user_input = input("Enter your move (rock, paper, or scissors): ").lower()
            if user_input == 'rock':
                return Rock()
            elif user_input == 'paper':
                return Paper()
            elif user_input == 'scissors':
                return Scissors()
            else:
                print("Please enter rock, paper, or scissors.")


def main():
    human_player = HumanPlayer()
    computer_player = Player()
    human_score = 0
    computer_score = 0
    while True:
        human_turn = human_player.play()
        computer_turn = computer_player.play()
        print("Human chose: ", human_turn.str())
        print("Computer chose: ", computer_turn.str())

        if human_turn > computer_turn:
            print("Human wins!")
            human_score += 1
        elif computer_turn > human_turn:
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        print("human_score = ",human_score)
        print("computer_score = ",computer_score)
        print("========================================================")

if __name__ == "__main__":
    main()