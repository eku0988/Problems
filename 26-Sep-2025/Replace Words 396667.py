# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Put all roots into a set for quick lookup
        root_set = set(dictionary)
        words = sentence.split()
        result = []

        for word in words:
            replacement = word
            # Check prefixes of the word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    replacement = prefix
                    break  # shortest prefix found, stop checking
            result.append(replacement)

        return " ".join(result)
