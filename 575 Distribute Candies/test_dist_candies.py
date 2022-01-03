import unittest
from dist_candies import Solution

class TestSulution(unittest.TestCase):
    def test_distribute_candies(self):
        s = Solution()
        self.assertEqual(s.distributeCandies([1,1,2,2,3,3]), 3)
        self.assertEqual(s.distributeCandies([1,1,2,3]), 2)
        self.assertEqual(s.distributeCandies([6,6,6,6]), 1)
        self.assertEqual(s.distributeCandies([6, 5]), 1)
        self.assertEqual(s.distributeCandies([]), 0)
        # self.assertEqual(type(s.distributeCandies([1,1,2,3])), type(0))


if __name__ == '__main__':
    unittest.main()