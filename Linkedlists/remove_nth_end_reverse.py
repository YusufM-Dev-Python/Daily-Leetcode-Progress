# Day 25: Remove Nth Node From End (Reverse Method)
# Topic: Linked List Manipulation
# Logic: Triple Reverse (Reverse -> Remove from Start -> Reverse back)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 1. First Reverse: Turn "End" into "Start"
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        new_head = prev
        
        # 2. Handle the Removal
        if n == 1:
            # If removing the first element of reversed list (original last)
            new_head = new_head.next
        else:
            # Travel to the node just before the one we want to delete
            temp = new_head
            for i in range(n - 2):
                temp = temp.next
            # Skip the nth node
            temp.next = temp.next.next
                
        # 3. Second Reverse: Restore the original order
        curr = new_head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev