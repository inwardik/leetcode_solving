class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        max_subarray = float('-inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                continue
            tempSum = 0
            for j in range(i, len(nums)):
                tempSum += nums[j]
                max_subarray = max(max_subarray, tempSum)
                
        return max_subarray
    
    def maxSubArray(self, nums: List[int]) -> int:
        sum_list = []
        for i in range(len(nums)):
            if i == 0:
                sum_list.append(nums[i])
            else:
                sum_list.append(max([nums[i], nums[i] + sum_list[-1]]))
        return max(sum_list)
    
    def maxSubArray3(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        g = nums[0]
        for i in range(N):
            l = max(nums[i], nums[i]+l)
            g = max(l, g)
        return g
                
    

s = Solution()

assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, 'first'
assert s.maxSubArray([1]) == 1, 'second'
assert s.maxSubArray([5,4,-1,7,8]) == 23, 'third'
assert s.maxSubArray([-2, 1]) == 1, 'fourth'
assert s.maxSubArray([-2, -1]) == -1, 'fifth'
assert s.maxSubArray([0,-3,1,1]) == 2, 'six'

