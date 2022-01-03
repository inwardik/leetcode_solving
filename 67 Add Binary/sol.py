class Solution:
    def addBinary(self, a: str, b: str) -> str:
        over = False
        la, lb = (list(a), list(b)) if len(a) < len(b) else (list(b), list(a))
        la.reverse()
        lb.reverse()
        for i in range(len(lb)):
            lai = int(la[i]) if i < len(la) else 0
            s = lai + int(lb[i]) + int(over)
            if s < 2:
                lb[i] = s
                over = False
            elif s == 2:
                lb[i] = 0
                over = True
            else:
                lb[i] = 1
                over = True
        if over:
            lb.append(1)
        result = ''.join(reversed(list(map(str, lb))))
        return result

    def addBinary2(self, a: str, b: str) -> str:
        n = max(len(a),len(b))
        a,b = a.zfill(n), b.zfill(n)
        carry = 0
        res = []
        for i in range(n-1,-1,-1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            
            if carry % 2 == 1:
                res.append('1')
            else:
                res.append('0')
            carry //= 2
        
        if carry == 1:
            res.append('1')
        res.reverse()
        return "".join(res)


s = Solution()
assert s.addBinary('11', '1') == '100', '11-1'
assert s.addBinary('1010', '1011') == '10101', '1010-1011'