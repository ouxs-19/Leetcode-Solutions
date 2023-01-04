# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        self.found_p = False 
        self.found_q = False 
        self.pd = 0
        self.dq = 0
        
        def find_p(r,p,q,par,d):
            if r != None :
                parents[r.val] = par
                if r.val == p.val :
                    self.found_p = True
                    self.pd = d
                elif r.val == q.val :
                    self.found_q = True
                    self.dq = d

                if self.found_p and  self.found_q : 
                    return 
            
                find_p(r.right,p,q,r,d+1)
                find_p(r.left,p,q,r,d+1)
            
        find_p(root,p,q,None,0)

        while self.pd > self.dq : 
            p = parents[p.val]
            self.pd-=1
            
        while self.pd < self.dq : 
            q = parents[q.val]
            self.dq-=1
        
        while p.val != q.val :
            p = parents[p.val]
            q = parents[q.val]
        return p
        
        
