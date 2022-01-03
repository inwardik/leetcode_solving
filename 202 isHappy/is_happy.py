import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        repeated = set()
        while n not in repeated and len(repeated) < 100:
            repeated.add(n)
            n = self.convert(n)
            if n == 1:
                return True
        return False

    def convert(self, n):
        sum = 0
        for sign in str(n):
            sum += int(sign) ** 2
        return sum


class TestSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.isHappy(19), True)
        self.assertEqual(s.isHappy(2), False)


if __name__ == '__main__':
    unittest.main()
    # s = Solution()
    # print(s.isHappy(70))