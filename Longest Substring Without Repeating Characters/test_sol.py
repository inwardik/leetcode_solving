import unittest
from sol import Solution


class TestSolution(unittest.TestCase):
    def test_repeat(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring(""), 0)

if __name__ == '__main__':
    unittest.main()