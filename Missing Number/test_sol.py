import unittest

from sol import Solution


class TestSolution(unittest.TestCase):
    def test_sol(self):
        s = Solution()
        self.assertEqual(s.missingNumber([3,0,1]), 2)
        self.assertEqual(s.missingNumber([0,1]), 2)
        self.assertEqual(s.missingNumber([9,6,4,2,3,5,7,0,1]), 8)
        self.assertEqual(s.missingNumber([0]), 1)
        self.assertEqual(s.missingNumber([1]), 0)



if __name__ == '__main__':
    unittest.main()