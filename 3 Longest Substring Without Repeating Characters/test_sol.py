import unittest
from sol import Solution


class TestSolution(unittest.TestCase):
    def test_repeat(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("au"), 2)
        self.assertEqual(s.lengthOfLongestSubstring("a"), 1)
        self.assertEqual(s.lengthOfLongestSubstring(""), 0)
        self.assertEqual(s.lengthOfLongestSubstring("abcdefghabcdefghijklmnopqrstuvwxyzabcdaefghijklmnopqrstuvwxyz"), 26)

if __name__ == '__main__':
    unittest.main()