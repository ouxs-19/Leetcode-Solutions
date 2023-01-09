# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def preorder(r):
            if r :
                self.res.append(r.val)
                preorder(r.left)
                preorder(r.right)
        preorder(root)
        return self.res