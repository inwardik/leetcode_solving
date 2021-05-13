# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_node(root, deep=0):
            if not root:
                return deep
            return max((get_node(root.left, deep+1), get_node(root.right, deep+1)))
        return get_node(root, 0)
