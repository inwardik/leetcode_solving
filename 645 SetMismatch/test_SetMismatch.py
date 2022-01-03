import unittest
from SetMismatch import Solution

class TestSolution(unittest.TestCase):
    def test_find_error(self):
        s = Solution()
        self.assertEqual(s.findErrorNums([1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums([1,2,3,4,5,3,7,8]), [3, 6])
        self.assertEqual(s.findErrorNums([1,2,4,4,5,6,7,8]), [4, 3])
        self.assertEqual(s.findErrorNums([1,2,3,4,5,6,7,8,8]), [8, 9])
        self.assertEqual(s.findErrorNums([1,1]), [1,2])
        self.assertEqual(s.findErrorNums([2,2]), [2,1])
        self.assertEqual(s.findErrorNums([1,5,3,2,2,7,6,4,8,9]), [2,10])


if __name__ == '__main__':
    unittest.main()