# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()

        if '@' in s:
            # Email case
            name, domain = s.split('@')
            name = name.lower()
            domain = domain.lower()
            return name[0] + "*****" + name[-1] + "@" + domain
        else:
            # Phone number case
            digits = ''
            for ch in s:
                if '0' <= ch <= '9':
                    digits += ch

            local = "***-***-" + digits[-4:]
            country_code_len = len(digits) - 10

            if country_code_len == 0:
                return local
            else:
                return "+" + "*" * country_code_len + "-" + local