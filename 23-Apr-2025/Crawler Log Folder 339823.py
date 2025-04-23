# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        result=0
        for log in logs:
            if log =='./':
                continue
            elif log =='../':
                result=max(0,result-1)
            else:
                result+=1
        return result