# Day 26: Rotate List
# Topic: Cyclic Linked Lists & Modular Arithmetic
# Complexity: O(n) Time, O(1) Space

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head 

        # 1. Find Length & Get to the Tail
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        # 2. Form a Circular Linked List (Connect Tail to Head)
        curr.next = head 

        # 3. Handle Large K with Modular Arithmetic
        # If length is 5 and k is 12, rotating 12 times is the same as rotating 2 times.
        rotation = k % length 
        
        # 4. Find the "Break Point"
        # If we rotate RIGHT by 2, we need to move the tail FORWARD by (length - 2).
        steps = length - rotation  

        # 5. Move curr to the node BEFORE the new head
        while steps > 0:
            curr = curr.next
            steps -= 1

        # 6. Break the Ring
        new_head = curr.next
        curr.next = None
        
        return new_head