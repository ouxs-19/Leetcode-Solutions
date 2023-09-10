# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        n = 0 
        
        while curr :
            n+=1 
            curr = curr.next
        
        m = math.ceil(n/k)      
        nodes = []

        curr, last = head, head
        cnt = 1 
        ln = k 
        while curr:
            if cnt == m  or curr.next is None:  
                save = curr.next
                curr.next = None 
                nodes.append(last)
                curr, last = save, save
                n -= cnt
                ln -= 1
                m = math.ceil(n/(ln or 1))      
                cnt = 1
            else:
                curr = curr.next
                cnt+=1

        nodes = nodes + [None] * ln
        return nodes