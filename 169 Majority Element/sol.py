class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        max_value = max(num_dict.values())
        for key, value in num_dict.items():
            if value == max_value:
                return key
            
    def majorityElement2(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
                
            
s = Solution()        
assert s.majorityElement([3, 2, 3]) == 3
assert s.majorityElement([1]) == 1
assert s.majorityElement([2,2,1,1,1,2,2]) == 2

