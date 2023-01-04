# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        l = []
        def solve(r):
            if r : 
                l.append(r)
                solve(r.left)            
                solve(r.right)
        solve(root)
        if l :
            curr = l.pop()
            while l : 
                per = l.pop()
                per.right = curr
                per.left = None
                curr = per
            