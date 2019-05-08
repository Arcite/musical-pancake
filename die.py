"""
Module that represents a die that can be rolled
"""
import unittest
import numpy as np

np.random.RandomState()

def roll(sides, times=1):
    """
    FCTVAL === numpy array of times random numbers between [1, sides]
    """
    return np.random.randint(1, sides, times)

def roll_with_modifier(sides, times=1, modifier=0):
    """
    FCTVAL === numpy array of times random numbers between [1+modifier, sides+modifier]
    """
    return roll(sides, times) + modifier

class TestDiceMethods(unittest.TestCase):
    """
    Class to test the die.py class
    """

    def test_roll_d20(self):
        """
        Rolls a d20 10,000 times and verifies they're all [1,20]
        """
        results = roll(20, 10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 21)) 

    def test_roll_d6(self):
        """
        Rolls a d20 10,000 times and verifies they're all [1,6]
        """
        results = roll(6, 10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 6))

    def test_roll_with_modifier(self):
        """
        Rolls a d20 10,000 times with a modifier of +5 and verifies they're all [6,25]
        """
        results = roll_with_modifier(20, 10000, 5)
        self.assertTrue(np.all(results > 5) & np.all(results < 26)) 

if __name__ == '__main__':
    unittest.main()
    