# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        self.d = defaultdict(bool)
        self.stack = []
        def solve(r):
            if r : 
                if r.val : 
                    for node in self.stack : 
                        self.d[node] = True
                self.stack.append((r,1))
                solve(r.left)
                self.stack.pop()
                self.stack.append((r,0))
                solve(r.right) 
                self.stack.pop()
            else : 
                for node in self.stack : 
                    self.d[node] = self.d[node] or False 
        solve(r)
        for node in self.d: 
            if not self.d[node]:
                if node[1]:
                    node[0].left = None
                else :
                    node[0].right = None
        if r.val == 0 and r.left == None and r.right == None : return None 
        return r