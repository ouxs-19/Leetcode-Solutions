# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(curr,a,b):
            if curr:
                if a<curr.val<b:
                    return solve(curr.left,a,curr.val) and solve(curr.right,curr.val,b)
                else : 
                    return False
            return True
        return solve(root,float("-inf"),float("inf"))