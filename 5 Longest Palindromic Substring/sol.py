class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        def is_palindromic(inp_str):
            if inp_str[0] != inp_str[-1]:
                return False
            if inp_str[::-1] == inp_str:
                return True
            return False
        max_pal = s[0]
        for i in range(len(s)-1):
            for j in range(len(s)-1, i + len(max_pal) - 1, -1):
                if is_palindromic(s[i:j+1]):
                    max_pal = s[i:j+1]
                    break
        return max_pal
                    
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        longest = 0
        res = ""
        for i in range(n):
            # odd
            left, right = i - 1, i + 1
            odd = 1
            while 0 <= left and right <= n - 1:
                if s[left] == s[right]:
                    odd += 2
                else:
                    break
                left -= 1
                right += 1
            if odd > longest:
                longest = odd
                res = s[left+1:right]
            
            # even
            if i == n - 1:
                continue
            left, right = i, i + 1
            even = 0
            while 0 <= left and right <= n - 1:
                if s[left] == s[right]:
                    even += 2
                else:
                    break
                left -= 1
                right += 1
            if even > longest:
                longest = even
                res = s[left+1:right]
        
        return res