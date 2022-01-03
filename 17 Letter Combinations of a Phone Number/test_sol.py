from pprint import pprint
import unittest
from sol import Solution

# u = unittest.TestCase()
# pprint(dir(u))

class TestSolution(unittest.TestCase):
    def test_sol(self):
        s = Solution()
        self.assertListEqual(s.letterCombinations('2'), ["a","b","c"])
        self.assertListEqual(s.letterCombinations('23'), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertListEqual(s.letterCombinations(''), [])

if __name__ == '__main__':
    unittest.main()