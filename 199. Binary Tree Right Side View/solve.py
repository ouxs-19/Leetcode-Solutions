# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, r: Optional[TreeNode]) -> List[int]:
        sol = {}
        if r :
            queue = [(r, 0)]
            while queue:
                curr, d = queue.pop(0)
                sol[d] = curr.val
                if curr.left :
                    queue.append((curr.left, d+1))
                if curr.right :
                    queue.append((curr.right, d+1))
        return sol.values()