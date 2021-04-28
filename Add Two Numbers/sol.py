# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def num_from_node(node):
            if not node:
                return 0
            res = 0
            mul = 1
            while True:
                print(node.val)
                res = res + node.val * mul
                mul *= 10
                if not node.next:
                    break
                node = node.next
            return res
        def node_from_num(num):
            previos = None
            for ch in str(num):
                node = ListNode(ch, previos)
                previos = node
            return node

        sum_of_two = num_from_node(l1) + num_from_node(l2)
        return node_from_num(sum_of_two)


s = Solution()
l1 = ListNode(2, (ListNode(4, ListNode(3))))
l2 = ListNode(5, (ListNode(6, ListNode(4))))
res = s.addTwoNumbers(l1, l2)
print(l1)