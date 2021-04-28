class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        if len(str) == 1:
            return 1
        

        return 1

s = Solution()
res = s.lengthOfLongestSubstring('abraca')
print(res)