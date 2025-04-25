# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_arr = path.split("/")
        stack = []

        for sec in path_arr:
            # section is not empty and section is not "." which means just current directory
            if sec != "" and sec != ".":
                if sec == "..":
                    # pop previous val in stack is sec is ".."
                    if stack:
                        stack.pop()
                else:               
                    stack.append(sec)

        res = "/" + "/".join(stack)
        return res