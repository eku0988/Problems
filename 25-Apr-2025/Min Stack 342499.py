# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []  
    
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # Push the new min onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()