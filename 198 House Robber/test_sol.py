import unittest

from sol import Solution


class TestSolution(unittest.TestCase):
    def test_rob(self):
        s = Solution()
        self.assertEqual(s.rob([1,2,3,1]), 4)
        self.assertEqual(s.rob([2,7,9,3,1]), 12)
        self.assertEqual(s.rob([6, 7, 1, 0, 8, 8, 6, 7]), 21)

if __name__ == '__main__':
    unittest.main()