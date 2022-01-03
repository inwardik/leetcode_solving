import unittest

from sol import Solution

class TestSolution(unittest.TestCase):
    def test_median(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1,3], [2]), 2)
        self.assertEqual(s.findMedianSortedArrays([1,2], [3, 4]), 2.5)
        self.assertEqual(s.findMedianSortedArrays([0,0], [0, 0]), 0)
        self.assertEqual(s.findMedianSortedArrays([], [1]), 1)
        self.assertEqual(s.findMedianSortedArrays([2], []), 2)
        self.assertEqual(s.findMedianSortedArrays([], []), 0)


if __name__ == '__main__':
    unittest.main()