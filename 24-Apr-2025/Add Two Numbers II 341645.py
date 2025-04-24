# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        
        carry=0
        result=None
        while stack1 or stack2 or carry:
            Sum=carry
            if stack1:
                Sum+=stack1.pop()
            if stack2:
                Sum+=stack2.pop()
            new_node=ListNode(Sum%10)
            new_node.next=result
            result=new_node
            carry=Sum//10
        return result