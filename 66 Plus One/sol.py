class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return (list(map(int, str(int(''.join(map(str, digits))) + 1))))
    
    
s = Solution()
print(s.plusOne([1, 2, 3]))
# assert s.plusOne([1, 2, 3]) == [1, 2, 4], 'first'
# assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], 'second'
# assert s.plusOne([0]) == [1], 'third'