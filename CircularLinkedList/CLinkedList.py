class CLinkedList:
    def __init__(self):
        self.head = None

    def printNodes(self):
        tmp = self.head
        while True:
            print("Node Data {} ".format(tmp.data))
            if tmp.next == self.head:
                break
            tmp = tmp.next

    def insertAtFirst(self, node):
        tmp = self.head
        while True:
            if tmp.next == self.head:
                tmp.next = node
                node.next = self.head
                self.head = node
                break
            tmp = tmp.next

    def deleteNode(self, node):
        global last
        tmp = self.head
        if self.head is None:
            print("Circular Linked List is empty.")
        while tmp:
            if tmp.next == self.head:
                last = tmp
                break
            tmp = tmp.next

        tmp = self.head
        if self.head ==node:
            self.head = node.next
            last.next = node.next
            return

        while True:
            if tmp.next == node:
                tmp.next = node.next
                return
            if tmp.next == self.head:
                break
            tmp = tmp.next




