import inp
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            breaker = 0
            while i > 0 and nums[i-1] == nums[i] and breaker < len(nums):
                breaker += 1
                temp = nums[i]
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                nums[-1] = temp

        res = 1
        for index, num in enumerate(nums):
            if index < len(nums) - 1 and num < nums[index+1]:
                res += 1
            else:
                break
        return res


s = Solution()
#ar = [0, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10, 10, 10, 10]
ar = inp.ar
res = s.removeDuplicates(ar)
print(res)
print(ar)