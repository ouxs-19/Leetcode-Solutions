# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.l = {1:[],2:[]}
        
        def inorder(r,index):
            if r :
                inorder(r.left,index)
                if not r.left and not r.right :
                    self.l[index].append(r.val)
                inorder(r.right,index)

        inorder(root1,1)
        inorder(root2,2)
        return self.l[1] == self.l[2]