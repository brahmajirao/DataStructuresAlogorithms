"""
Question
Given a dice which rolls 1 to 7 (with uniform probability), simulate a 5 sided dice. Preferably, write your solution as a function.

SOLUTION
This is a new problem we haven't seen directly before! Many times this question is asked in the
form of functions e.g. your given a function random_7() and you have to take it as an input and
create random_5()

The key to solving this problem is to make sure you focus on the requirement that the final
distribution of the rolls be uniform, also you were not given any requirements on Time and Space,
so the solution is actually very simple, just keep re-rolling if you get a number greater than 5!
"""

from random import randint

def roll_dice():
    return randint(1, 7)

def convert7to5():
    roll = 7
    while roll > 5:
        roll = roll_dice()
        print('roll_dice() produced a roll of ', roll)
    print('Your final returned roll is blow:')
    return roll

if __name__=="__main__":
    print(convert7to5())