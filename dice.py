"""Participation Activity 4 - Dice

Implements the unit 4 participation activity: a Die class with a sides
attribute and a roll_die method, then rolls 6-, 10-, and 20-sided dice.
Each die is rolled once per side it has.

Author: cet
Date: 2026-09-27
"""

import random


class Die:
    """A die with a configurable number of sides."""

    def __init__(self, sides=6):
        """Store the number of sides on the die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(random.randint(1, self.sides))

def main():
    """Roll that baby! Rolls the die."""
    dice = [Die(), Die(10), Die(20)]
    for die in dice:
        print(f"Rolling a {die.sides}-sided die {die.sides} times:")
        for _ in range(die.sides):
            die.roll_die()
        print()


if __name__ == "__main__":
    main()