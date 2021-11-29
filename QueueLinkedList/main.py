from QueueLinkedList.QLinkedList import QLinkedList
from QueueLinkedList.QNode import QNode

if __name__ == '__main__':
    queueLinkedList = QLinkedList()
    node1 = QNode(1)
    node2 = QNode(2)
    node3 = QNode(3)
    node4 = QNode(4)
    node5 = QNode(5)

    queueLinkedList.front = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    queueLinkedList.rear = node5

    # queueLinkedList.printNodes()

    print("enqueue node in linked List")
    node6 = QNode(6)
    queueLinkedList.enQueue(node6)
    queueLinkedList.printNodes()

    print("dequeue node in linked List")
    queueLinkedList.deQueue()
    queueLinkedList.deQueue()
    queueLinkedList.deQueue()

    queueLinkedList.printNodes()



