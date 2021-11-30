from ast import slice

from StackLinkedList.SLinkedList import SLinkedList
from StackLinkedList.SNode import SNode

if __name__ == '__main__':
    stackLinkedList = SLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    node4 = SNode(4)
    node5 = SNode(5)

    stackLinkedList.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    stackLinkedList.printNodes()

    print("push node in linked List")
    node6 = SNode(6)
    stackLinkedList.push(node6)
    stackLinkedList.printNodes()

    print("pop node in linked List")
    stackLinkedList.pop()
    stackLinkedList.pop()

    stackLinkedList.printNodes()



