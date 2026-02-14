# Day 5: Design Circular Queue (LeetCode #622)
# Topic: Fixed-size Buffer Management
# Time Complexity: O(1) for all operations

class MyCircularQueue(object):
    def __init__(self, k):
        self.k = k
        self.cir = [0] * k
        self.head = 0
        self.tail = 0
        # The 'counter' is the secret weapon of this implementation
        self.counter = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.cir[self.tail] = value
        # Wraparound logic: If tail is at the end, it jumps back to index 0
        self.tail = (self.tail + 1) % self.k
        self.counter += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        # Move head forward; % k handles the circular wraparound
        self.head = (self.head + 1) % self.k
        self.counter -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.cir[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        # Tail points to the next EMPTY spot, so we look at (tail - 1)
        # The % k ensures if tail is 0, we look at index k-1
        idx = (self.tail - 1) % self.k
        return self.cir[idx]

    def isEmpty(self):
        return self.counter == 0

    def isFull(self):
        return self.counter == self.k