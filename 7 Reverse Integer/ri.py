class Solution:
    def reverse(self, x: int) -> int:

        def is_in_int(x):
            if not -2**31 <= x <= 2**31 - 1:
                return False
            return True

        if not is_in_int(x):
            return 0
        pos_or_neg = 1
        if x < 0:
            x *= -1
            pos_or_neg = -1
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        result *= pos_or_neg        
        if is_in_int(result):
            return result
        return 0

s = Solution()
print(s.reverse(2**32 * -1))
print(2**31)