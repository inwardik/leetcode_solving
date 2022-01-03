import random
from datetime import datetime
from typing import List

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start_time)
        return res
    return wrapper


class Solution:
    @timeit
    def maxArea(self, height: List[int]) -> int:
        while height[0] == 0:
            del(height[0])
        while height[-1] == 0:
            del(height[-1])
        def is_mirror(height):
            if len(height) < 3:
                return False
            dif = height[1] - height[0]
            if dif == 0:
                return False
            for i in range(1, int(len(height)/2)):
                if (height[i] != height[-i-1]) or (height[i] - height[i-1] != dif):
                    return False
            return True

        if is_mirror(height):
            sum_height = sum(height)
            if not sum_height % 2:
                return int(sum_height / 2)
            else:
                return int((sum_height + 1) / 2)

        def find_area(index1, index2):
            hi2 = height[index2]
            hi1 = height[index1]
            if hi2 > hi1:
                return (index2 - index1) * hi1
            else:
                return (index2 - index1) * hi2
        maximum_area = 0
        minimal_first = 0
        for ind1 in range(len(height)-1):
            if height[ind1] > minimal_first:
                minimal_first = height[ind1]
                for ind2 in range(ind1 + 1, len(height)):
                    area = find_area(ind1, ind2)
                    if area > maximum_area:
                        maximum_area = area
        return maximum_area


def main():
    s = Solution()
    #data = [random.randint(1,100000) for i in range(40000)]
    #data = [i for i in range(5000)] + [i for i in range(5000,-1,-1)]
    data = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,0]
    print(s.maxArea(data))
    print(sum(data) / 2)

if __name__ == '__main__':
    main()