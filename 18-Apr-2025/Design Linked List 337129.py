# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.ref = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None 

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.ref
            count += 1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.ref = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            return
        
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node = Node(val)
                new_node.ref = current.ref
                current.ref = new_node
                return
            current = current.ref
            count += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.ref
            return

        current = self.head
        count = 0
        while current and current.ref:
            if count == index - 1:
                current.ref = current.ref.ref
                return
            current = current.ref
            count += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)