# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # If the tree is empty, return False
        if not root:
            return False

        targetSum -= root.val

        # Check if we reached a leaf node
        if not root.left and not root.right:
            return targetSum == 0

        # Recursively check the left and right subtree
        return (self.hasPathSum(root.left, targetSum) or 
                self.hasPathSum(root.right, targetSum))