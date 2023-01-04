# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(list)
        def solve(r) :
            sol = {}
            local_d = defaultdict(list)
            pos = 0 
            last_d = 0
            if r :
                queue = [(r, 0, pos)]
                while queue:
                    curr, d, pos = queue.pop(0)
                    if d>last_d:
                        for k in local_d:
                            self.d[k].extend(sorted(local_d[k]))
                        local_d = defaultdict(list)
                    local_d[pos].append(curr.val)
                    last,last_d = curr,d
                    sol[d] = curr.val
                    if curr.left :
                        queue.append((curr.left, d+1, pos-1))
                    if curr.right :
                        queue.append((curr.right, d+1, pos+1))
                for k in local_d:
                    self.d[k].extend(sorted(local_d[k]))
        solve(root)
        return [self.d[k] for k in sorted(self.d)]