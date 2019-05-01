import numpy as np
import os

class Die:

    def __init__(self, sides):
        np.random.RandomState()
        self.sides = sides

    def roll(self, times = 1):
        return np.random.randint(1, self.sides, times)