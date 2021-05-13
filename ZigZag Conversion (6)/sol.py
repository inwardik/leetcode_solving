class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = [[] for i in range(numRows)]
        direction = 1
        i = 0
        for letter in s:
            res[i].append(letter)
            i += direction
            if i == numRows-1 or i == 0:
                direction *= -1
        flattern = ''.join(map(str, [j for i in res for j in i]))
        return flattern
        