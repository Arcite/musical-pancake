import unittest
import dice

class TestDiceMethods(unittest.TestCase):

    def test_rollD20(self):
        d20 = dice.Die(20)
        for _ in range(0,1000):
            result = d20.roll()
            self.assertTrue(result > 0 & result < 21)
    
    def test_rolD6(self):
        d6 = dice.Die(6)
        for _ in range(0,1000):
            result = d6.roll()
            self.assertTrue(result > 0 & result < 7)

if __name__ == '__main__':
    unittest.main()