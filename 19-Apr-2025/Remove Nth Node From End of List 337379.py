# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        left=dummy
        right=head 
        while n>0 and right:
            right=right.next
            n-=1

        while right:
            right=right.next
            left=left.next

        left.next=left.next.next
        return dummy.next

        

