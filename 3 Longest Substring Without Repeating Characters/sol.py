class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        def is_substr_valid(substr):
            if len(substr) == len(set(substr)):
                return True
            return False

        window = 1
        for i in range(len(s)):
            if len(s) < i + window + 1:
                break
            while len(s) >= i + window + 1 and is_substr_valid(s[i:i+window+1]):
                window += 1

        return window

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0
        start = 0
        lastIdx = dict()
        for i, c in enumerate(s):
            if c in lastIdx and lastIdx[c]>=start:
                max_length = max(max_length, i - start)
                start = lastIdx[c] + 1
            lastIdx[c] = i
        
        return max(max_length, len(s) - start)

s = Solution()
res = s.lengthOfLongestSubstring('au')
print(res)