class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        for num in nums:
            if num != i:
                return i
            i += 1
        return i




s = Solution()
print(s.missingNumber([0,1]))