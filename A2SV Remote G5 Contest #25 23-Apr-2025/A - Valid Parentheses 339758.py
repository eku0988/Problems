# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        bracketMap = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracketMap.values():
                stack.push(char)
            else:
                if stack.is_empty() or stack.pop() != bracketMap[char]:
                    return False

        return stack.is_empty()
