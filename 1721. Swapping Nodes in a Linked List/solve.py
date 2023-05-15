class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength = 0 
        curr = head 
        while curr :
            listLength += 1
            curr = curr.next
        
        curr = head 
        first = k-1
        second = listLength - k 
        count = 0 
        
        while curr :
            if count == first :
                firstNode = curr
            if count == second :
                secondNode = curr
            curr = curr.next
            count +=1
        
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
        return head