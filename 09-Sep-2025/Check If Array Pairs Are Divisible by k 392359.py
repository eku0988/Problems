# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        
        # Step 1: Count remainder frequencies
        for num in arr:
            r = num % k
            freq[r] += 1
        
        # Step 2: Check special case for remainder 0
        if freq[0] % 2 != 0:
            return False
        
        # Step 3: Check each remainder pairing
        for r in range(1, (k // 2) + 1):
            if r == k - r:  # special case (when k is even, e.g., r=2 for k=4)
                if freq[r] % 2 != 0:
                    return False
            else:
                if freq[r] != freq[k - r]:
                    return False
        
        return True
