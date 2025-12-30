# Day 2: Asteroid Collision (LeetCode #735)
# Pattern: Stack Simulation
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            # Safety check: 'alive' flag tracks if the current asteroid survives collisions
            alive = True
            
            # A collision only happens if the stack top is moving RIGHT (+) 
            # and the current asteroid is moving LEFT (-)
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) > stack[-1]:
                    stack.pop() # Current asteroid destroys the stack top and continues
                    continue
                elif abs(ast) < stack[-1]:
                    alive = False # Current asteroid is destroyed by stack top
                    break
                elif abs(ast) == stack[-1]:
                    stack.pop() # Both asteroids destroy each other
                    alive = False
                    break
            
            if alive:
                stack.append(ast)
        return stack