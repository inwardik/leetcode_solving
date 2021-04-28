import unittest
from most_water import Solution

class TestSolution(unittest.TestCase):
    def test_max_area(self):
        s = Solution()
        self.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(s.maxArea([1,2]), 1)
        self.assertEqual(s.maxArea([2,3,4,5,18,17,6]), 17)
        self.assertEqual(s.maxArea([1,1]), 1)
        self.assertEqual(s.maxArea([4,3,2,1,4]), 16)
        self.assertEqual(s.maxArea([1,2,1]), 2)
        self.assertEqual(s.maxArea([1]), 0)
        self.assertEqual(s.maxArea([100, 100, 100]), 200)
        self.assertEqual(s.maxArea([28, 11, 87, 23, 56, 29, 20, 48, 73, 29, 96, 62, 2, 12, 89, 30, 32, 73, 57, 80]), 1360)
        self.assertEqual(s.maxArea([853, 348, 761, 591, 9, 243, 418, 83, 250, 880, 52, 790, 961, \
            709, 88, 542, 216, 601, 603, 939, 100, 752, 147, 138, 468, 696, 360, 735, 685, 267]), 19845)
        self.assertEqual(s.maxArea([i for i in range(100)] + [i for i in range(100,-1,-1)]), 5000)




if __name__ == '__main__':
    unittest.main()