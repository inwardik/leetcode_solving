from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.val} -> left:{self.left} right:{self.right} '


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        stack = deque((root,))
        while stack:
            node = stack.pop()
            if node.left:
                stack.appendleft(node.left)
            if node.right:
                stack.appendleft(node.right)
        return 1




s = Solution()
#root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(root)
#root = None
print(s.levelOrder(root))