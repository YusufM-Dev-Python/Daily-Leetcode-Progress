# Day 14: Reverse Linked List (Recursive)
# Topic: Recursion & Linked Lists
# Time Complexity: O(n)
# Space Complexity: O(n) due to the recursive call stack

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Base Case: If list is empty or we've reached the last node
        if not head or not head.next:
            return head

        # 2. Recursive Step: Go all the way to the end first
        # This 'new_head' will be the original last node (the new front)
        new_head = self.reverseList(head.next)

        # 3. The "Neighbor's Neighbor" Logic:
        # head.next is my neighbor. 
        # I want my neighbor's next pointer to point back to ME.
        head.next.next = head
        
        # 4. Break the old connection to avoid cycles
        head.next = None

        # Return the new head (it stays the same all the way up the stack)
        return new_head