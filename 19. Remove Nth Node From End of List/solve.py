# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0 
        tmp = head 
        while tmp :
            tmp = tmp.next 
            l+=1
        ind = 0 
        t = l - n 
        if t == 0 :
            return head.next 
        tmp = head 
        while ind < t :
            ind+=1
            last = tmp
            tmp = tmp.next
        last.next = tmp.next
        return head