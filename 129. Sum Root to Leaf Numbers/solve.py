# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0 
        self.stack = []
        def parc(r,gathered):
            if r :
                if r.left and r.right:
                    parc(r.left,gathered+str(r.val))
                    parc(r.right,gathered+str(r.val))
                elif r.left : 
                    parc(r.left,gathered+str(r.val))
                elif r.right :
                    parc(r.right,gathered+str(r.val))
                else :
                    parc(r.right,gathered+str(r.val))
            else :
                self.sum+=int(gathered)
        parc(root,"")
        return self.sum