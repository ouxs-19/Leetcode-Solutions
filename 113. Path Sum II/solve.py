# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        self.res = []
        if root : self.stack = [root.val]
        else : return self.res
        def solve(r, s):
            if not r.left and not r.right and s == t : 
                return self.res.append(self.stack.copy())
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
        return self.res