"""
Module that represents a die that can be rolled
"""
import unittest
import numpy as np

class Die:
    """
    Class that represents a die that can be rolled
    """

    def __init__(self, sides):
        np.random.RandomState()
        self.sides = sides

    def roll(self, times=1):
        """
        Roll the die a number of times equal to times
        FCTVAL === numpy array of times random numbers between [1, self.sides]
        """
        return np.random.randint(1, self.sides, times)

class TestDiceMethods(unittest.TestCase):
    """
    Class to test the die.py class
    """

    def test_roll_d20(self):
        """
        Rolls a d20 10,000 times and verifies they're all [1,20]
        """
        d20 = Die(20)
        results = d20.roll(10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 21)) 
    def test_roll_d6(self):
        """
        Rolls a d20 10,000 times and verifies they're all [1,6]
        """
        die6 = Die(6)
        results = die6.roll(10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 6))

if __name__ == '__main__':
    unittest.main()
    