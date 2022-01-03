class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}->{self.next}'


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        prev_l1 = None
        prev_l2 = None
        res_head = l2
        while current_l2:
            while current_l1:
                if current_l1.val <= current_l2.val:
                    prev_l1 = current_l1
                    current_l1 = current_l1.next
                    prev_l2.next = prev_l1
                    prev_l1.next = current_l2
                    prev_l2 = prev_l1
                    



l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

s = Solution()
res = s.mergeTwoLists(l1, l2)
print(res)