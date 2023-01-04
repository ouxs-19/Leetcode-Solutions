# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        s = head
        while l1 != None and l2 != None :
            if l1.val <= l2.val :
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
            else :
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
                
        if l1 == None :
            while l2!= None :
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
        else :
            while l1 != None :
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next
        return s.next