import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = string.ascii_letters + string.digits
        str_list = [letter for letter in s.lower() if letter in alphanum]
        if str_list == str_list[::-1]:
            return True
        return False
    
    def isPalindrome2(self, s: str) -> bool:
        strs: List[str] = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        num: int = len(strs)
        for i in range(num//2):
            if strs[i] != strs[num-i-1]:
                return False
        return True

sol = Solution()
assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
assert sol.isPalindrome("race a car") == False