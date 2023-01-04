class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> TreeNode:

        def create(bottom, sup):
            if bottom > sup: return None
            val = p[self.ind]
            r = TreeNode(val)
            self.ind += 1
            r.left = create(bottom, i_d[val]-1)
            r.right = create(i_d[val]+1,sup)

            return r
        self.ind = 0 
        ln = len(p)
        i_d = {i[j] : j  for j in range(ln)}
        return create(0,ln-1)