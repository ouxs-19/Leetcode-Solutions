# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        cnt = 0 
        while curr : 
            curr = curr.next
            cnt += 1
        if cnt == 1 : head = None  
        else : 
            index = cnt // 2
            curr = head 
            for i in range(index):
                prev = curr
                curr = curr.next
            prev.next = curr.next
        return head