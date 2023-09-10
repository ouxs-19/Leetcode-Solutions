# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)
            elif root.left:
                return self.minDepth(root.left)+1
            elif root.right:
                return self.minDepth(root.right)+1
            else:
                return 1
        return 0    