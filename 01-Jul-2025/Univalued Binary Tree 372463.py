# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        queue = deque([root])
        unival = root.val

        while queue:
            node = queue.popleft()
            if node.val != unival:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True
