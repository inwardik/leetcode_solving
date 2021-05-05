class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) >= len(haystack):
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                needle_found = True
                for j in range(len(needle)):
                    if i + j >= len(haystack):
                        needle_found = False
                        break
                    if haystack[i+j] != needle[j]:
                        needle_found = False
                        break
                if needle_found:
                    return i
        return -1
