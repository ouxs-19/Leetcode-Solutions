# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(r):
            if r :
                if r.left and r.right : 
                    return f"{r.val}({solve(r.left)})({solve(r.right)})"
                elif r.left :
                    return f"{r.val}({solve(r.left)})"
                elif r.right :
                    return f"{r.val}()({solve(r.right)})"
                else :
                    return f"{r.val}"
            else : return ""
        return solve(root)