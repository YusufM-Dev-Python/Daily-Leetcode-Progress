# Day 14: Merge Two Sorted Lists (Recursive)
# Topic: Recursion & Linked Lists
# Time Complexity: O(n + m)
# Space Complexity: O(n + m) due to the call stack

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # 1. Base Cases: If one list is empty, the 'merge' is just the other list.
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # 2. The Comparison (Choosing the "Smallest" node)
        if list1.val <= list2.val:
            # list1 is smaller, so it stays. 
            # We ask recursion: "Who should come AFTER list1?"
            # We move list1 forward but keep list2 where it is.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 is smaller. 
            # We ask recursion: "Who should come AFTER list2?"
            # We move list2 forward but keep list1 where it is.
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2