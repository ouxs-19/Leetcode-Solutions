# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def path(r):
            if r : 
                path(r.left)
                path(r.right)
                self.res.append(r.val)

        path(root)
        return self.res