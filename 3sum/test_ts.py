import unittest

from ts import Solution

class TestThreeSum(unittest.TestCase):
    def test_ts(self):
        s = Solution()
        self.assertEqual(s.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(s.threeSum([]), [])
        self.assertEqual(s.threeSum([0]), [])
        self.assertEqual(s.threeSum([6, -11, 1, 3, 6, -12, -6, 2, 3, -4, 8, -7] ), [[-12, 6, 6], [-11, 3, 8], [-7, 1, 6], [-6, 3, 3], [-4, 1, 3]])
        self.assertListEqual(s.threeSum([18, -16, 9, 12, 18, -18, -5, 11, 13, -1, -8, -16, 15, 13, 2, -14, -3, 5]  ), [[-18, 5, 13], [-16, 5, 11], [-14, -1, 15], [-14, 2, 12], [-14, 5, 9], [-8, -5, 13], [-8, -3, 11], [-8, -1, 9]])
        self.assertListEqual(s.threeSum([16, -18, 7, 10, 16, -20, -7, 9, 11, -3, -10, -18, 13, 11, 0, -16, -5, 3, -18, 6]), [[-20, 7, 13], [-20, 9, 11], [-18, 7, 11], [-16, 0, 16], [-16, 3, 13], [-16, 6, 10], [-16, 7, 9], [-10, -3, 13], [-10, 0, 10], [-10, 3, 7], [-7, -3, 10], [-7, 0, 7], [-3, 0, 3]])

if __name__ == '__main__':
    unittest.main()