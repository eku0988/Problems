# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        num_str=str(abs(num))
        digits=sorted(num_str)

        if num >0:
            if digits[0]=='0':
                for i in range(1,len(digits)):
                    if digits[i] !='0':
                        digits[0],digits[i]=digits[i],digits[0] 
                        break
            return int("".join(digits))
        else:
            return -int("".join(sorted(digits, reverse=True)))