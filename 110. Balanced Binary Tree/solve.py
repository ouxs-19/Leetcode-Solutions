# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            left = self.depth(root.left)
            right = self.depth(root.right)
            if abs(left-right) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            return False
        return True
    
    def depth(self, r):
        if r :
            return max(self.depth(r.left)+1, self.depth(r.right)+1)
        return 0