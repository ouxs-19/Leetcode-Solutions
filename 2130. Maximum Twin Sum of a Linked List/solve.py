# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
        slow, fast = head, head
        previous = None
        ret = float("-inf")


        while fast:
            slower = slow
            slow = slow.next
            fast = fast.next.next
            slower.next = previous
            previous = slower 
        
        left = previous
        right = slow
        
        while left :
            ret = max(ret, left.val+right.val)
            left = left.next
            right = right.next
        
        return ret