class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ns_string = s.strip()
        if not len(ns_string):
            return 0
        return len(ns_string.split(' ')[-1])
    
    
s = Solution()
assert s.lengthOfLastWord("Hello World") == 5, 'first'
assert s.lengthOfLastWord("SingleWord") == 10, 'second'
assert s.lengthOfLastWord(" ") == 0, 'one space'
assert s.lengthOfLastWord("") == 0, 'empty string'
assert s.lengthOfLastWord("a ") == 1, 'space in the end'