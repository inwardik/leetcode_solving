import unittest

from sol import Solution


class TestSolution(unittest.TestCase):
    def test_true_anagram(self):
        s = Solution()
        self.assertEqual(s.isAnagram('anagram', 'nagaram'), True)
        self.assertEqual(s.isAnagram('agsajdfhaskfdh', 'hagsasjdfdhakf'), True)
        self.assertEqual(s.isAnagram('a', 'a'), True)
        self.assertEqual(s.isAnagram('', ''), True)

    def test_false_anagram(self):
        s = Solution()
        self.assertEqual(s.isAnagram('rat', 'car'), False)
        self.assertEqual(s.isAnagram('hello', 'olleg'), False)
        self.assertEqual(s.isAnagram('a', ''), False)
        self.assertEqual(s.isAnagram('a', 'b'), False)


if __name__ == '__main__':
    unittest.main()