class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        romans = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM', 1: 'I', 5: 'V',
        10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        keys = sorted(romans.keys(), reverse=True)
        for key in keys:
            while num >= key:
                num -= key
                result += romans[key]
        return result

s = Solution()
print(s.intToRoman(1234))