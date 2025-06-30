# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def backtrack(start, parts):
            # If 4 parts formed and end of string reached, append to result
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
            
            # Prune: if remaining chars too few or too many for remaining parts
            remaining = len(s) - start
            if remaining < (4 - len(parts)) or remaining > 3 * (4 - len(parts)):
                return
            
            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start:start+length]
                
                # Skip if segment has leading zero (except "0")
                if segment[0] == '0' and length > 1:
                    continue
                
                # Skip if segment value > 255
                if int(segment) > 255:
                    continue
                
                backtrack(start + length, parts + [segment])
        
        backtrack(0, [])
        return result
