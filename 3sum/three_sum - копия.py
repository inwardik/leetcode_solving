from typing import List
import random
from random import randint
random.seed(10)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for na in range(len(nums)):
            s_nums = nums[na+1:]
            s_nums.reverse()
            for nb in range(na+1, len(nums)):
                s_nums.pop()
                a, b = nums[na], nums[nb]
                c = (a + b) * -1
                if c in s_nums:
                    res = sorted([a,b,c])
                    triplets.append(res)
        triplets.sort()
        un_triplets = []
        current_t = []
        for t in triplets:
            if t != current_t:
                un_triplets.append(t)
            current_t = t

        return un_triplets


#nums = [-1,0,1,2,-1,-4]
    
def main():
    #nums = [-1,0,1,2,-1,-4] #[[-1,-1,2],[-1,0,1]]
    nums = [randint(-1000, 1000) for i in range(1000)]
    s = Solution()
    print(s.threeSum(nums))

if __name__ == '__main__':
    main()