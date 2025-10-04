# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    # Bucket-sort style (O(n + m log m) where m = distinct words)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1

        # buckets by frequency
        freq = [[] for _ in range(len(words) + 1)]
        for w, c in count.items():
            freq[c].append(w)

        # sort each bucket lexicographically so ties are broken correctly
        for bucket in freq:
            if bucket:
                bucket.sort()

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for w in freq[i]:
                res.append(w)
                if len(res) == k:
                    return res
        return res


