import unittest
from lcp import Solution

def test_lcp_python():
    s = Solution()
    assert s.longestCommonPrefix([]) == ''
    assert s.longestCommonPrefix(['']) == ''
    assert s.longestCommonPrefix(['ivan']) == 'ivan'

class TestLcp(unittest.TestCase):
    def test_prefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]), 'fl')
        self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]), '')
        self.assertEqual(s.longestCommonPrefix(['iva', 'ivan', 'ivanov']), 'iva')
        self.assertEqual(s.longestCommonPrefix(['sirotkin', 'sirotkina', 'sirotkiny']), 'sirotkin')
        self.assertEqual(s.longestCommonPrefix(['sirotkin']), 'sirotkin')


        self.assertEqual(s.longestCommonPrefix([]), '')

if __name__ == '__main__':
    unittest.main()