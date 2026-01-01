# Day 4: Implement Stack using Queues (LeetCode #225)
# Topic: Queue Rotation (FIFO to LIFO)
# Time Complexity: Push: O(n), Pop/Top: O(1)

from collections import deque

class MyStack(object):
    def __init__(self):
        # We use a deque (double-ended queue) for O(1) popleft() operations
        self.queue = deque()

    def push(self, x):
        # 1. Add the new element to the back of the queue
        self.queue.append(x)

        # 2. CRUCIAL POINT: Rotate the queue
        # We move all previous elements to the back, one by one.
        # This REVERSES the order so the newest element (x) is now at the front.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        # Because we rotated on push, the "top" is at the front of the queue
        return self.queue.popleft()

    def top(self):
        # The front of the queue represents the top of the stack
        return self.queue[0]

    def empty(self):
        return not self.queue