# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # Return if the tree is empty
        if not root:
            return root
        # Find the node to be deleted
        if key < root.val:
            root.left=self.deleteNode(root.left, key)
        elif(key > root.val):
            root.right=self.deleteNode(root.right, key)
        else:
            # If the node is with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            #Find the min from right subtree
            curr=root.right
            while curr.left:
                curr=curr.left
            root.val=curr.val
            root.right=self.deleteNode(root.right, root.val)

        return root
