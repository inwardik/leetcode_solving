class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        pare_list = ['()']
        
        def step():
            nonlocal pare_list
            temp_list = []
            for item in pare_list:
                item_ar = list(item)
                for c in range(len(item)+1):
                    item_ar.insert(c, '()')
                    temp_list.append(''.join(item_ar))
                    del(item_ar[c])
            temp_list = list(set(temp_list))    
            pare_list = temp_list
            
        for i in range(n-1):
            step()
        pare_list = sorted(list(set(pare_list)))
        
        return pare_list

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
   
s = Solution()
#res = s.generateParenthesis(4)
#print(res)
assert s.generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'], '3'
assert s.generateParenthesis(4) == ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"], '4'
