# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 , l2 = self.recup(l1) , self.recup(l2)
        return self.make(list(map(int,str(int("".join(map(str,l1[::-1])))+int("".join(map(str,l2[::-1]))))))[::-1])

    def recup(self,l):
        n = [l.val]
        while l.next != None :
            n.append(l.next.val)
            l = l.next 
        return n

    def make(self,l):
        head = ListNode(l[0])
        last = head
        for val in l[1:] :
            n = ListNode(val)
            last.next = n
            last = n
        return head
            