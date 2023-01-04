# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, r: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        depth -=1
        if depth == 0 :
            n = TreeNode(val,r,None)
            return n 
        if r :
            queue = [(r, 1)]
            while queue:
                curr, d = queue.pop(0)
                if d == depth : 
                    n_l = TreeNode(val,curr.left,None)
                    n_r = TreeNode(val,None,curr.right)
                    curr.left = n_l
                    curr.right = n_r
                elif d > depth : 
                    return r
                if curr.left :
                    queue.append((curr.left, d+1))
                if curr.right :
                    queue.append((curr.right, d+1))
