# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Minimum number of times we need to repeat 'a'
        repeat_count = -(-len(b) // len(a))  # same as math.ceil(len(b)/len(a))
        
        # Check for b being a substring in the repeated versions
        if b in a * repeat_count:
            return repeat_count
        elif b in a * (repeat_count + 1):
            return repeat_count + 1
        else:
            return -1
