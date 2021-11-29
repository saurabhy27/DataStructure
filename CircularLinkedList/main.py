from CircularLinkedList.CLinkedList import CLinkedList
from LinkedList.SNode import SNode

if __name__ == "__main__":
    cicularLinkedList = CLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    node4 = SNode(4)
    node5 = SNode(5)
    cicularLinkedList.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node1
    # cicularLinkedList.printNodes()

    print("insert at beginning")
    node0 = SNode(0)
    cicularLinkedList.insertAtFirst(node0)
    cicularLinkedList.printNodes()

    print("delete a beginning")
    node8 = SNode(8)
    cicularLinkedList.deleteNode(node8)
    cicularLinkedList.printNodes()
