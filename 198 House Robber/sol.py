class Solution:
    def rob(self, nums: list[int]) -> int:
        current_max = 0
        previous_max = 0
        for num in nums:
            previous_max, current_max = current_max, max(previous_max + num, current_max)
        return current_max
        




s = Solution()
result = s.rob([6, 7, 1, 0, 8, 8, 6, 7])
print(result)