class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        for letter in s:
            if letter in s_dic:
                s_dic[letter] += 1
            else:
                s_dic[letter] = 1
        for letter in t:
            try:
                s_dic[letter] -= 1
            except KeyError:
                return False
        if set(s_dic.values()) in ({0}, {}, set()):
            return True
        return False



s = Solution()
print(s.isAnagram('', ''))