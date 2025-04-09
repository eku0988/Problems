# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """    
        vowels = set('aeiou')
        count = 0
        n = len(word)

        for i in range(n):
            if word[i] not in vowels:
                continue
            unique_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                unique_vowels.add(word[j])
                if len(unique_vowels) == 5:
                    count += 1

        return count
