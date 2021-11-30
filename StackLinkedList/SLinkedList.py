class SLinkedList:
    def __init__(self):
        self.head = None

    def printNodes(self):
        tmp = self.head
        while tmp:
            print("Node Data {} ".format(tmp.data))
            tmp = tmp.next

    def push(self, node):
        tmp = self.head
        node.next = tmp
        self.head = node

    def pop(self):
        tmp = self.head
        if tmp is None:
            print("No data found")
            return
        self.head = tmp.next
        del tmp
