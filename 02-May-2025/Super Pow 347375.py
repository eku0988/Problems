# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        c=''
        for i in b:
            c+=str(i)
    
        result = pow(a,int(c),1337)
        return result
        
