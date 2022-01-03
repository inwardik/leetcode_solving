import operator
class Node:
    def __init__(self, value, my_index, nei_indexes):
        self.value = value
        self.my_index = my_index
        self.nei_indexes = nei_indexes

    def __repr__(self):
        return f'{self.value} [{self.my_index}]'


class Solution:
    def rob(self, nums: list[int]) -> int:
        total = 0
        node_nums = []
        for i, num in enumerate(nums):
            neibours = []
            if i > 0:
                neibours.append(i - 1)
            if i < len(nums) - 1:
                neibours.append(i + 1)
            node_item = Node(num, i, neibours)
            node_nums.append(node_item)
        node_nums.sort(reverse=True, key=operator.attrgetter('value'))
        active_nodes = []
        neibour_indexes = []
        for i, node in enumerate(node_nums):
            if i == 0:
                print(node)
                active_nodes.append(node)
                for index in node.nei_indexes:
                    neibour_indexes.append(index)
            else:
                if node.my_index not in neibour_indexes:
                    print(node)
                    active_nodes.append(node)
                    for index in node.nei_indexes:
                        neibour_indexes.append(index)

        return sum(n.value for n in active_nodes)





s = Solution()
result = s.rob([6, 7, 1, 7, 8, 8, 6, 5])
print(result)