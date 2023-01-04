# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], t: int) -> bool:
        self.res = []
        self.found = False
        if root : self.stack = [root.val]
        else : return self.res
        def solve(r, s):
            if not self.found : 
                if not r.left and not r.right and s == t : 
                    self.found = True
                else : 
                    if r.left : 
                        self.stack.append(r.left.val)
                        solve(r.left,  s+r.left.val)
                        self.stack.pop()
                    if r.right : 
                        self.stack.append(r.right.val)
                        solve(r.right, s+r.right.val)
                        self.stack.pop()
                    
        solve(root, root.val)
        return self.found 