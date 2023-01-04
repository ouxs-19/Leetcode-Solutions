# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(bottom, sup):
            if bottom > sup: return None
            ind = (bottom+sup)//2
            val = nums[ind]
            r = TreeNode(val)
            r.left = create(bottom,ind-1)
            r.right = create(ind+1,sup)

            return r
        
        ln = len(nums)
        return create(0,ln-1)