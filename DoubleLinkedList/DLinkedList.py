class DLinkedList:
    def __init__(self):
        self.head = None

    def printNodes(self):  # complexity O(N)
        tmp = self.head
        while tmp:
            print("Node data {} ".format(tmp.data))
            tmp = tmp.next

    def insertAtStart(self, node):  # complexity O(1)
        tmp = self.head
        node.next = tmp
        self.head.prev = node
        self.head = node

    def insertAtEnd(self, node):  # complexity O(N)
        tmp = self.head
        while tmp:
            if tmp.next is None:
                tmp.next = node
                node.prev = tmp
                break
            tmp = tmp.next

    def insertAfterNode(self, node, nodeInsert):  # complexity O(1)
        nodeInsert.next = node.next
        node.next.prev = nodeInsert
        node.next = nodeInsert
        nodeInsert.prev = node

    def deleteNode(self, node):
        if self.head is None:
            print("No node found!")
            return
        prevNode = node.prev
        nextNode = node.next
        if prevNode is not None:
            prevNode.next = nextNode
        else:
            self.head = nextNode
        if nextNode is not None:
            nextNode.prev = prevNode

    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.prev = next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev