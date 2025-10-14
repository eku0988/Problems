# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        
        # Initialize waiting dictionary with iterators for each word
        for w in words:
            it = iter(w)
            waiting[next(it)].append(it)
        
        count = 0
        
        # Traverse each character in s
        for c in s:
            # Get list of iterators waiting for this character
            iters = waiting.pop(c, [])
            
            for it in iters:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1  # Finished word
        
        return count
