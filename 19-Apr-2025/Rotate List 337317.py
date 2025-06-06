# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return
        
        length=1
        tail=head
        while tail.next :
            tail=tail.next
            length+=1

        k= k % length  
        if k ==0:
            return head

        curr=head
        for i in range(length-k-1):
            curr=curr.next  
        newHead=curr.next
        curr.next=None
        tail.next=head
        
        return newHead