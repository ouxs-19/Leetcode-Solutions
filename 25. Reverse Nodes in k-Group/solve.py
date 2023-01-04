# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 : return head 
        vals = []
        curr = head 
        while curr :
            vals.append(curr.val)
            curr = curr.next
        i = 0 
        n = len(vals)
        head = None
        cur = None 
        last = None 
        while i < n-k+1 : 
            true_last = last 
            for j in range(i,i+k):
                new =  ListNode(vals[j],curr)
                if j == i : last = new 
                curr = new
            if not head :
                head = curr 
            else :
                true_last.next = curr 
            curr = None 
            
            i+=k
        curr = last   
        while i < n : 
            new = ListNode(vals[i])
            curr.next = new 
            curr = new 
            i+=1
        return head 