class QLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def printNodes(self):
        tmp = self.front
        while tmp:
            print("Node Data {} ".format(tmp.data))
            tmp = tmp.next

    def enQueue(self, node):
        if self.front is None:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        node = self.rear

    def deQueue(self):
        if self.front is None:
            print("No data found")
            return
        tmp = self.front
        self.front = tmp.next
        del tmp
