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

def hit_or_miss(rolls, ac):
    """
    PRE:    rolls is a numpy array simulating dice rolls
            ac is the minimum value to be considered a "hit"
    FCTVAL === numpy array of Boolean values where True is a hit and False is a miss
    """
    return rolls >= ac

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

    def test_hit_or_miss(self):
        """
        Uses pregenerated arrays to verify hit_or_miss
        """
        t1 = np.array([1, 2, 3, 4, 5])
        v1 = np.array([False, False, False, False, False])
        self.assertTrue(np.all(hit_or_miss(t1, 6) == v1))

        t2 = np.array([6, 7, 8, 9, 10])
        v2 = np.array([True, True, True, True, True])
        self.assertTrue(np.all(hit_or_miss(t2, 5) == v2))

        t3 = np.array([11, 13, 15, 17, 19])
        v3 = np.array([False, False, True, True, True])
        self.assertTrue(np.all(hit_or_miss(t3, 15) == v3))


if __name__ == '__main__':
    unittest.main()
    