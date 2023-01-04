# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        l = []
        i = 0
        n = len(lists)
        while i<n  :
            pointer = lists[i]
            while pointer != None :
                l.append(pointer.val)
                pointer = pointer.next
            i+=1
        l.sort()
        head = ListNode()
        s = head
        
        i = 0
        n = len(l)
        while i < n :
            head.next = ListNode(l[i])
            head = head.next
            i+=1
        return s.next
            