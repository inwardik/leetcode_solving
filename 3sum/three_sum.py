from typing import List
import random
from random import randint
import letnums
random.seed(10)



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        first = [i for i in nums if i <= 0]
        third = list(reversed([i for i in nums if i >= 0]))
        for nf, f in enumerate(first):
            for nt, t in enumerate(third):
                if t < abs(f)//2:
                    continue
                s_nums = nums[nf+1:-nt-1]
                second = (f + t) * -1
                if second in s_nums:
                    triplets.append([f, second, t])
                    continue
        triplets.sort()
        un_triplets = []
        current_t = []
        for t in triplets:
            if t != current_t:
                un_triplets.append(t)
            current_t = t

        return un_triplets



def main():
    nums = [-1,0,1,2,-1,-4] #[[-1,-1,2],[-1,0,1]]
    #nums = letnums.nums
    nums = [randint(-18, 18) for i in range(18)]
    s = Solution()
    print(nums, '\n')
    print(s.threeSum(nums))

if __name__ == '__main__':
    main()

