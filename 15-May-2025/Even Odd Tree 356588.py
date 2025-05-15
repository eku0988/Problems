# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        queue = deque([root])
        even=True
        while queue:
            prev_val = float("-inf") if even else float("inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                if even:
                    if node.val % 2 == 0 or node.val <= prev_val:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= prev_val:
                        return False
                    
            #only adding elements to the queue if it is not null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                prev_val=node.val

            even =not even

        return True