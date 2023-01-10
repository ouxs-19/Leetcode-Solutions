import re
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, T: str) -> Optional[TreeNode]:
        
        self.root = None

        def create(r, s, d=1, left=True):
            if (delim:='-'*d) in s :
                s = re.split(f'(?<=\d){delim}(?=\d)', s)
                val = s[0]
            else:
                val = s
            node = TreeNode(int(val))
            if r:
                if left:
                    r.left = node
                else :
                    r.right = node
            else:
                self.root = node
            if isinstance(s,list):
                create(node, s[1], d+1)
                if len(s) == 3 :
                    create(node, s[2], d+1, False)

            return 

        create(self.root, T)
        return self.root