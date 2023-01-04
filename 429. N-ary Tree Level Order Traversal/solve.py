"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, r: 'Node') -> List[List[int]]:
        sol = defaultdict(list)
        if r :
            queue = [(r, 0)]
            while queue:
                curr, d = queue.pop(0)
                sol[d].append(curr.val)
                for child in curr.children :
                    queue.append((child, d+1))
        return sol.values()