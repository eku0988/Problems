# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Re-positioning for next swap
            prev = first
            head = first.next

        return dummy.next