# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        curr, last = head, None
        while m > 1:
            last = curr
            curr = curr.next
            m, n = m - 1, n - 1
        tail, con = curr, last
        while n:
            third = curr.next
            curr.next = last
            last = curr
            curr = third
            n -= 1
        if con:
            con.next = last
        else:
            head = last
        tail.next = curr
        return head