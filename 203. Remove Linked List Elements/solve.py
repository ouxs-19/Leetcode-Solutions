# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        last = None 
        curr = head 
        found = False 
        while curr :
            if curr.val == val :
                if last :
                    last.next = curr.next
                else :
                    head = curr.next 
                curr = curr.next
            else :
                last = curr
                curr = curr.next 
        return head 