# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0 
        def inorder(r):
            if r:
                if r.val >=low:inorder(r.left)
                if low<=r.val<=high:
                    self.s += r.val
                if r.val <= high : inorder(r.right)
        inorder(root)
        return self.s