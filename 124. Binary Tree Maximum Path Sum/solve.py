# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(r):
            if r != None :
                b,b_ = solve(r.left)
                c,c_ = solve(r.right)
                maxb = max(r.val+c_,r.val+b_,r.val)
                maxa = max(b,c,maxb,r.val+b_+c_)
                return maxa , maxb
            return float("-inf"),float("-inf")
        return solve(root)[0]