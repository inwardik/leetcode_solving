from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == '':
            return []
        digit_map = {
        '2': ['a', 'b' ,'c'],
        '3': ['d', 'e' ,'f'],
        '4': ['g', 'h' ,'i'],
        '5': ['j', 'k' ,'l'],
        '6': ['m', 'n' ,'o'],
        '7': ['p', 'q' ,'r', 's'],
        '8': ['t', 'u' ,'v'],
        '9': ['w', 'x' ,'y', 'z'],
        }
        payload = []
        for digit in digits:
            payload.append(digit_map[digit])
        result = []
        for item in product(*payload):
            result.append(''.join(item)) 
        return result


s = Solution()
print(s.letterCombinations('2'))
