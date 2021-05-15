class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result_list = []
        for i in range(len(intervals)):
            if not i:
                result_list.append(intervals[i])
                continue
            if intervals[i][0] <= result_list[-1][1]:
                result_list[-1][1] = max([result_list[-1][1], intervals[i][1]])
            else:
                result_list.append(intervals[i])
        print(result_list)
        return sum([item[1] - item[0] for item in result_list])

    def merge2(self, intervals):
        min_num = float('inf')
        max_num = float('-inf')
        for i in intervals:
            for j in i:
                min_num = min([min_num, j])
                max_num = max([max_num, j])
        field = [0]*(max_num - min_num + 1)
        for i in intervals:
            for j in range(i[0], i[1]):
                field[j] = 1
        print(field)
        return sum(field)



sol = Solution()
res = sol.merge([[-5,-3],[1,3], [-3, -2], [2,6], [-15,-5] ,[8,10],[15,18]])
res2 = sol.merge2([[-5,-3],[1,3], [-3, -2], [2,6], [-15,-5] ,[8,10],[15,18]])
print(res)
print(res2)
#assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
#assert sol.merge([[1,4],[4,5]]) == [[1,5]]
#assert sol.merge([[1,4],[4,5]]) == [[1,5]]
assert sol.merge([[-5,-3],[1,3], [-3, -2], [2,6], [-15,-5] ,[8,10],[15,18]]) == 23
