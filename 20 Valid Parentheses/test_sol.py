import unittest

from sol import Solution


class TestSolution(unittest.TestCase):
    def test_is_valid(self):
        s = Solution()
        self.assertEqual(s.isValid(r'[]'), True)
        self.assertEqual(s.isValid(r'(())'), True)
        self.assertEqual(s.isValid(r'()[]{}'), True)
        self.assertEqual(s.isValid(r'[]'), True)
        self.assertEqual(s.isValid(r'{[]}'), True)
        self.assertEqual(s.isValid(r'{[([{{([({([{([])}])})])}}])]}'), True)
        
        self.assertEqual(s.isValid(r'{[([{{([{([{([])}])})])}}])]}'), False)
        self.assertEqual(s.isValid(r'{[([{{([{([{([])}])})])}])]}'), False)
        self.assertEqual(s.isValid(r'([)]'), False)
        self.assertEqual(s.isValid(r']'), False)
        self.assertEqual(s.isValid(r'['), False)
        self.assertEqual(s.isValid(r'(]'), False)

if __name__ == '__main__':
    unittest.main()