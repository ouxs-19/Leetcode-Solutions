# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
mod = 10**9 + 7
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node : return 0 
            curr = dfs(node.right)+dfs(node.left)+node.val
            self.res = max(self.res, curr * (self.all_sum - curr))
            return curr
        self.res = 0 
        self.all_sum = 0 
        self.all_sum = dfs(root)
        dfs(root)
        return self.res % mod