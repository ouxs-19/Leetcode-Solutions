# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.d = 0 
        self.s = 0 
        def get_d(r,d):
            if r :
                get_d(r.right,d+1)                
                get_d(r.left,d+1)
                self.d = max(self.d,d)
        
        def get_s(r,d):
            if r :
                get_s(r.right,d+1)                
                get_s(r.left,d+1)
                if d == self.d : self.s += r.val
        
        get_d(root,0)
        get_s(root,0)
        
        return self.s