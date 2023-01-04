# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def solve(r):
            sol = defaultdict(list)
            if r :
                queue = [(r, 0)]
                while queue:
                    curr, d = queue.pop(0)
                    sol[d].append(curr.val)
                    if curr.left :
                        queue.append((curr.left, d+1))
                    if curr.right :
                        queue.append((curr.right, d+1))
            return sol
        sol = solve(root)
        res = []
        for k in sol : 
            res.append(sum(sol[k])/len(sol[k]))
        return res