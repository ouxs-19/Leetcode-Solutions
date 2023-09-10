# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head
        
        last, curr = head, head.next

        while curr :
            if curr.val == last.val:
                last.next = curr.next
            else:
                last = curr

            curr = curr.next

        return head