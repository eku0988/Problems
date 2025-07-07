# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cookies)
        ans = [float('inf')]  # Use list to allow mutation
        distribution = [0] * k

        def backtrack(index):
            if index == n:
                ans[0] = min(ans[0], max(distribution))
                return
            for i in range(k):
                distribution[i] += cookies[index]
                if distribution[i] < ans[0]:
                    backtrack(index + 1)
                distribution[i] -= cookies[index]
                if distribution[i] == 0:
                    break

        backtrack(0)
        return ans[0]
