# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        count = Counter(words[0])
        for w in words:
            cur_count = Counter(w)
            for c in count:
                count[c] = min(count[c], cur_count[c])
        
        result = []
        for c in count:
            for i in range(count[c]):
                result.append(c)
                
        return result
                
