from DoubleLinkedList.DLinkedList import DLinkedList
from DoubleLinkedList.DNode import DNode

if __name__ == '__main__':
    doublyLinkedList = DLinkedList()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    node5 = DNode(5)
    doublyLinkedList.head = node1
    node1.next = node2
    node2.prev = node1

    node2.next = node3
    node3.prev = node2

    node3.next = node4
    node4.prev = node3

    node4.next = node5
    node5.prev = node4

    # doublyLinkedList.printNodes()

    print("Insert a node at start od Linked List ")
    node0 = DNode(0)
    doublyLinkedList.insertAtStart(node0)
    # doublyLinkedList.printNodes()

    print("Insert at end of Linked List ")
    node6 = DNode(6)
    doublyLinkedList.insertAtEnd(node6)
    # doublyLinkedList.printNodes()

    print("Insert after a node in Linked List ")
    node4_5 = DNode(4.5)
    doublyLinkedList.insertAfterNode(node4, node4_5)
    # doublyLinkedList.printNodes()

    print("Delete a node ")
    doublyLinkedList.deleteNode(node0)
    doublyLinkedList.deleteNode(node4_5)
    # doublyLinkedList.deleteNode(node6)
    doublyLinkedList.printNodes()

    # print("reverse ")
    # doublyLinkedList.reverse()
    # doublyLinkedList.printNodes()

