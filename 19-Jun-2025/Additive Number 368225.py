# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        # Try all possible pairs for the first and second number
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]

                # Skip if numbers have leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue

                a, b = int(num1), int(num2)
                k = j

                while k < n:
                    next_num = a + b
                    next_str = str(next_num)
                    if not num.startswith(next_str, k):
                        break
                    k += len(next_str)
                    a, b = b, next_num

                if k == n:
                    return True

        return False