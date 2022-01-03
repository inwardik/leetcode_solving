from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res_list = []
        
        def find_double(nums):
            s = set()
            for item in nums:
                if item in s:
                    return item
                else:
                    s.add(item)
            return None

        def find_absent(nums):
            s_absent = set(nums)
            s_full = set(range(1, max(nums)+1))
            res = s_absent ^ s_full
            if len(res) == 1:
                return res.pop()
            else:
                return max(nums) + 1

        return [find_double(nums), find_absent(nums)]



s = Solution()
print(s.findErrorNums([1,2,2,4]))