class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort(key=lambda x: len(x))
        templ = strs[0]
        for i in range(len(templ)):
            if not all(map(lambda x: x[i] == templ[i], strs)):
                return templ[:i]
        return templ

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        prefix_str = ''
        if not strs:
            return prefix_str
        smallest_str = min(strs, key=len)
        for i in range(len(smallest_str)):
            for string in strs:
                if smallest_str[i] != string[i]:
                    return prefix_str
            prefix_str = smallest_str[: i + 1]
        return prefix_str

s = Solution()
print(s.longestCommonPrefix(['ivo', 'ivan', 'ivanov']))

