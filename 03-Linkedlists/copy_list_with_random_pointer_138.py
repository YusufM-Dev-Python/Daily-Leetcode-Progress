# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Interleave - Create copy nodes and insert them after originals
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Connect Random Pointers - Copy's random is original's random.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Extract - Separate the interleaved list into original and copy
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        
        while curr:
            # isolate the copy
            copy = curr.next
            copy_curr.next = copy
            copy_curr = copy
            
            # restore the original
            curr.next = copy.next
            curr = curr.next
            
        return dummy.next