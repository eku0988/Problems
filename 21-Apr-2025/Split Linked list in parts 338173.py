# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        base_len, remainder = length // k, length % k
        curr = head
        res = []
        for i in range(k):
            res.append(curr)
            for j in range(base_len - 1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            remainder -= 1 if remainder else 0
        return res