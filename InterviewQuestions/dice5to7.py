"""
Question
Given a dice which rolls from 1 to 5, simulate a uniform 7 sided dice!

SOLUTION
Because the 5 sided dice can not produce 7 possible outcomes on a single roll, we immediately know that we need to roll the dice at least twice.

If we roll the dice twice we have 25 possible combinations of the results of the two rolls. While 25 is not divisible by 7, 21 is. This means we can implement our previous strategy of throwing out rolls not in our intended range.

It's also important to note that we can't expand the solution to implement more rolls in order to not throw any out, because 5 and 7 are both prime which means that no exponent of 5 will be divisible by 7 no matter how high you go.

We will define our range as a section of the 25 possible combinations of rolls. A good way to do this is by converting the two rolls into a unique outcome number in the range 1 through 25.

We will create this number by taking the rolls, then we take the first roll and after subtracting 1 from it we multiply it by 5. Now the first roll corresponds with a value of 0, 5, 10, 15 and 20.

Then we take the second roll and add it to the result of the first manipulation. Giving us a range of 1-25.

So our final solution is to roll the dice twice. Check the manipulated range from 1 to 25, if its greater than 21, do a reroll. Let's see it in action:
"""

from random import randint
def roll_dice():
    return randint(1, 5)

def convert5to7():
    while True:
        roll_1 = roll_dice()
        roll_2 = roll_dice()

        num = ((roll_1 - 1)*5) + (roll_2)

        if num > 21:
            continue
        return num%7 + 1

if __name__=="__main__":
    print(convert5to7())

