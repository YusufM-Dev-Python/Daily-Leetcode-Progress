class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create interleaved nodes (A -> A' -> B -> B')
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next

        # Step 2: Assign random pointers for the copies
        curr = head
        while curr:
            if curr.random:
                # The copy's random is the original's random's copy
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the interleaved lists
        curr = head
        dummy = Node(0)
        tail = dummy
        while curr:
            next_old = curr.next.next
            copy = curr.next

            tail.next = copy
            tail = copy

            # Restore original list
            curr.next = next_old
            curr = next_old
            
        return dummy.next