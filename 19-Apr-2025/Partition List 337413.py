# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        left=ListNode()
        right=ListNode()
        ltail=left
        rtail=right

        while head:
            if head.val < x:
                ltail.next=head
                ltail=ltail.next
            else:
                rtail.next=head
                rtail=rtail.next

            head=head.next
        ltail.next=right.next
        rtail.next=None

        return left.next