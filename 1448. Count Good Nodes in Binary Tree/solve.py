# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0 
        def solve(r,mx):
            if r : 
                if r.val >= mx : 
                    self.cnt += 1
                solve(r.left,max(mx,r.val))
                solve(r.right,max(mx,r.val))
        solve(root,float("-inf"))
        return self.cnt