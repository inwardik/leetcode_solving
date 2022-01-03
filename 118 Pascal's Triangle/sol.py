from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):
            if i == 1:
                result.append([1])
                continue
            temp_list = [None for _ in range(i)]
            for j in range(i):
                if j == 0 or j == i-1:
                    temp_list[j] = 1
                else:
                    temp_list[j] = result[-1][j-1] + result[-1][j]
            result.append(temp_list)
        return result



s = Solution()
res = s.generate(5)
print(res)