# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current:
            prev = current
            current = current.next
            while current and prev.val == current.val:
                prev.next = current.next
                current = current.next
        
        return head