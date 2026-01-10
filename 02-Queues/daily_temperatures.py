# Day 3: Daily Temperatures (LeetCode #739)
# Pattern: Monotonic Decreasing Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        # The stack will store INDICES of temperatures that haven't found a warmer day yet
        stack  = []
        # Initialize result with 0s; if no warmer day is found, it stays 0
        result = [0] * len(temperatures)

        for curr_day in range(len(temperatures)):
            curr_temp = temperatures[curr_day]

            # CRUCIAL POINT: If current temp is warmer than the temp at the index on top of stack
            while stack and curr_temp > temperatures[stack[-1]]:
                # We found a warmer day for the day at stack[-1]
                prev_day_index = stack.pop()
                # The 'wait time' is the difference between the current index and the old index
                result[prev_day_index] = curr_day - prev_day_index

            # Always push the current day's index to the stack to find its warmer day later
            stack.append(curr_day)
            
        return result