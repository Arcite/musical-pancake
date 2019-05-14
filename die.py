"""
Module that represents a die that can be rolled
"""
import unittest
import numpy as np

np.random.RandomState()

def roll(dice, times=1):
    """
    PRE:    dice is an array of numbers where each number represents the highest number on that dice
                ex) [20] = 1d20, [6, 6] = 2d6, [8, 6, 6, 6] = 1d8 + 3d6
            times is the number of times to roll the dice combination
    FCTVAL === numpy array of times random numbers between [len(dice), sum(dice)]
    """
    ret_val = np.zeros((1, times), dtype=np.int32)
    for die in dice:
        ret_val = ret_val + np.random.randint(1, die, times)
    return ret_val

def roll_with_modifier(dice, times=1, modifier=0):
    """
    PRE:    dice is an array of numbers where each number represents the highest number on that dice
                ex) [20] = 1d20, [6, 6] = 2d6, [8, 6, 6, 6] = 1d8 + 3d6
            times is the number of times to roll the dice combination
            modifier is a number to add to each roll
    FCTVAL === numpy array of times random numbers between [len(dice)+modifier, sum(dice)+modifier]
    """
    return roll(dice, times) + modifier

def hit_or_miss(rolls, armor_class):
    """
    PRE:    rolls is a numpy array simulating dice rolls
            armor_class is the minimum value to be considered a "hit"
    FCTVAL === numpy array of Boolean values where True is a hit and False is a miss
    """
    return rolls >= armor_class

def calculate_damage(hits, dice, modifier=0):
    """
    PRE:    hits is a numpy array of Boolean values where True represents a hit, and False a miss
            dice is an array of numbers where each number represents the highest number on that dice
                ex) [20] = 1d20, [6, 6] = 2d6, [8, 6, 6, 6] = 1d8 + 3d6
            modifier is a number to add to each roll
    FCTVAL === numpy array of random numbers between [1+modifier, sides+modifier] or 0 if False
    """
    return hits * roll_with_modifier(dice, len(hits), modifier)

class TestDiceMethods(unittest.TestCase):
    """
    Class to test the die.py class
    """

    def test_roll_d20(self):
        """
        Rolls a d20 10,000 times and verifies they're all [1,20]
        """
        results = roll([20], 10000)
        self.assertTrue(np.all(results >= 1) & np.all(results <= 20)) 

    def test_roll_d6(self):
        """
        Rolls a 2d8 10,000 times and verifies they're all [2,16]
        """
        results = roll([8, 8], 10000)
        self.assertTrue(np.all(results >= 1) & np.all(results <= 16))

    def test_roll_with_modifier(self):
        """
        Rolls a d20 10,000 times with a modifier of +5 and verifies they're all [6,25]
        """
        results = roll_with_modifier([20], 10000, 5)
        self.assertTrue(np.all(results >= 6) & np.all(results <= 25))

    def test_hit_or_miss(self):
        """
        Uses pregenerated arrays to verify hit_or_miss
        """
        test_1 = np.array([1, 2, 3, 4, 5])
        val_1 = np.array([False, False, False, False, False])
        self.assertTrue(np.all(hit_or_miss(test_1, 6) == val_1))

        test_2 = np.array([6, 7, 8, 9, 10])
        val_2 = np.array([True, True, True, True, True])
        self.assertTrue(np.all(hit_or_miss(test_2, 5) == val_2))

        test_3 = np.array([11, 13, 15, 17, 19])
        val_3 = np.array([False, False, True, True, True])
        self.assertTrue(np.all(hit_or_miss(test_3, 15) == val_3))

    def test_calculate_damage(self):
        """
        Uses pregenerated arrays to verify calculate_damage
        """
        test_1 = np.array([False, False, False, False, False])
        val_1 = np.array([0, 0, 0, 0, 0])
        self.assertTrue(np.all(calculate_damage(test_1, [6]) == val_1))

        test_2 = np.array([True, True, True, True, True])
        self.assertTrue(np.all(calculate_damage(test_2, [6]) > 0))

        results = calculate_damage(hit_or_miss(roll([20], 10000), 10), [8])
        self.assertTrue(np.all(results >= 0) and np.all(results <= 8))

if __name__ == '__main__':
    unittest.main()
    