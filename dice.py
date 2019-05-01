import random
import os

class Die:

    def __init__(self, sides):
        random.seed(os.urandom(32))
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)