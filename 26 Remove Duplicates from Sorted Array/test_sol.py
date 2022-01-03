import unittest

from sol import Solution

class TestSolution(unittest.TestCase):
    def test_array(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1, 2, 2, 3, 4]), 4)
        self.assertEqual(s.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        self.assertEqual(s.removeDuplicates([0, 1, 1,  2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10, 10]), 11)
        self.assertEqual(s.removeDuplicates([]), 0)
        self.assertEqual(s.removeDuplicates([5]), 1)
        self.assertEqual(s.removeDuplicates([5,5]), 1)
        self.assertEqual(s.removeDuplicates([5,5,5,5,5,5,5,5,5,5]), 1)
        self.assertEqual(s.removeDuplicates([5,6,7,8,8,8,8,8,8,8,8,8,9]), 5)


if __name__ == '__main__':
    unittest.main()