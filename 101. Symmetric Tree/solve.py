# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, r1: Optional[TreeNode], r2: Optional[TreeNode] = -1) -> bool:
        if r2 == -1 : r2 = r1
        if r1 is None and r2 is None : 
            return True
        if r1 and r2 and r1.val == r2.val and self.isSymmetric(r1.left,r2.right) and self.isSymmetric(r1.right,r2.left):
            return True
        return False