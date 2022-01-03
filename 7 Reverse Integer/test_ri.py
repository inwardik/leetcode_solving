import unittest
from ri import Solution


def test_ok_pytest():
	s = Solution()
	assert s.reverse(123) == 321
	assert s.reverse(-123) == -321
	assert s.reverse(120) == 21
	assert s.reverse(0) == 0

class TestReverse(unittest.TestCase):
	def test_ok(self):
		s = Solution()
		self.assertEqual(s.reverse(2**32), 0)
		self.assertEqual(s.reverse(-1 * 2**32), 0)
		self.assertEqual(s.reverse(1534236469), 0)
