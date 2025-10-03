# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:   
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in dp:
                return dp[i]

            # Option 1: skip current character
            res = 1 + dfs(i + 1) if i < len(s) else 0
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)

        