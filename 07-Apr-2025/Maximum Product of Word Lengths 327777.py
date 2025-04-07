# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        bitmasks = []
        lengths = []
        for word in words:
            mask = 0
            for ch in word:
                # Set the bit at position (ord(ch) - ord('a'))
                mask |= 1 << (ord(ch) - ord('a'))
            bitmasks.append(mask)
            lengths.append(len(word))

        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    product = lengths[i] * lengths[j]
                    max_product = max(max_product, product)

        return max_product
