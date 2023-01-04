# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        if head and head.next :
            head = head.next
            suiv, far = curr.next , curr.next.next
            suiv.next = curr
            curr.next = far
            last = curr
            curr = far 
        while curr and curr.next :
            suiv, far = curr.next , curr.next.next
            suiv.next = curr
            curr.next = far
            last.next = suiv
            last = curr
            curr = far 
        return head