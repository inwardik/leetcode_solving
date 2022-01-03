class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cash = set()
        for num in nums:
            if num in cash:
                cash.remove(num)
            else:
                cash.add(num)
        return list(cash)[0]
