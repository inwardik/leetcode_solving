import unittest
from cc import Solution

class TestSolution(unittest.TestCase):
    def test_candies(self):
        s = Solution()
        self.assertEqual(s.coinChange([1,2,5], 11), 3)
        self.assertEqual(s.coinChange([2], 3), -1)
        self.assertEqual(s.coinChange([1], 0), 0)
        self.assertEqual(s.coinChange([1], 1), 1)
        self.assertEqual(s.coinChange([1], 2), 2)
        self.assertEqual(s.coinChange([2,5], 6), 3)




if __name__ == '__main__':
    unittest.main()