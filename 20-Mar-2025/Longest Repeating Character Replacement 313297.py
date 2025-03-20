# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = defaultdict(int)  # Frequency of characters in the window
        left = 0
        max_freq = 0  # Max frequency of a single character in the window
        max_length = 0  # Result variable

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])

            # Condition: If window size - max_freq > k, shrink the window
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1  # Shrink window from the left

            max_length = max(max_length, right - left + 1)

        return max_length
