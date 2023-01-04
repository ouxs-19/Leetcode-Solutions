# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        curr = head 
        last = None 
        while curr and curr.val < x :
            last = curr
            curr = curr.next 
        insert = curr 
        while curr : 
            suiv = curr.next
            if curr.val < x :
                if last :
                    last.next, curr.next, prev.next = curr, last.next, curr.next
                else : 
                    head, curr.next, prev.next = curr, head, curr.next
                last = curr
            else : prev = curr 
            curr = suiv
        return head