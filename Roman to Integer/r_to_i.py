class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        romans = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'C': 100, 'D': 500, 'M': 1000,
        }
        for key, value in romans.items():
            if key in s:
                total += value * s.count(key)
                s = s.replace(key, '')
        return total


    def romanToInt2(self, s: str) -> int:
        ROMAN_MAP = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        total = 0
        prev = 0
        for i in range(len(s)):
            curr = ROMAN_MAP[s[i]]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total

        def romanToInt3(self, s: str) -> int:
            dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            
            out = 0
            cur = dic[s[0]]
            for i,x in enumerate(s):
                if dic[x] > cur:
                    out += dic[x]
                    out -= 2*cur
                    cur = dic[x]
                else:
                    out += dic[x]
                    cur = dic[x]
            return out
        



sol = Solution()
print(sol.romanToInt('MDLVII'))