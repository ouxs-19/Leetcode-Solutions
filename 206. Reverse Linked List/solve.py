# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        last = None
        curr = head
        while curr : 
            suiv = curr.next
            curr.next = last 
            last = curr
            curr = suiv
        return last
            