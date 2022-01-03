from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if not all([letter in r'{}[]()' for letter in s]):
            return False
        parentheses = {'}':'{', ']':'[', ')':'('}
        my_deque = deque('')
        for letter in s:
            if letter in '{[(':
                my_deque.append(letter)
            else:
                if not len(my_deque) or my_deque.pop() != parentheses[letter]:
                    return False
        if len(my_deque):
            return False
        return True


s = Solution()
result = s.isValid('[')
print(result)


#[{[]}]