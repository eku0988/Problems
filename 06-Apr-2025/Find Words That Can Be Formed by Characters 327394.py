# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= chars_count.get(char, 0) for char in word_count):
                total += len(word)

        return total
        