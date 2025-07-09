# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False

        pathToStart, pathToDest = [], []
        findPath(root, startValue, pathToStart)
        findPath(root, destValue, pathToDest)

        i = 0
        while i < len(pathToStart) and i < len(pathToDest) and pathToStart[i] == pathToDest[i]:
            i += 1
        return 'U' * (len(pathToStart) - i) + ''.join(pathToDest[i:])
