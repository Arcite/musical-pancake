import unittest
import dice
import numpy as np

class TestDiceMethods(unittest.TestCase):

    def test_rollD20(self):
        d20 = dice.Die(20)
        results = d20.roll(10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 21))
    
    def test_rolD6(self):
        d6 = dice.Die(6)
        results = d6.roll(10000)
        self.assertTrue(np.all(results > 0) & np.all(results < 6))

if __name__ == '__main__':
    unittest.main()