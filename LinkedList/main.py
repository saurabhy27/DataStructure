from LinkedList.SLinkedList import SLinkedList
from LinkedList.SNode import SNode

if __name__ == "__main__":
    # creating nodes
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    node4 = SNode(4)
    node5 = SNode(5)
    # adding nodes into linked list
    singleLL = SLinkedList()
    singleLL.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # printing nodes
    print("Start LL ")
    # singleLL.print_ll()

    # insert at begging of linked list
    node6 = SNode(6)
    singleLL.insert_at_start(node6)
    print("Insert node6 at start ")
    # singleLL.print_ll()

    # insert at some position of linked list
    node7 = SNode(7)
    print("Insert node7 at location 2 ")
    singleLL.insert_at_loc(2, node7)
    # singleLL.print_ll()

    # insert at end of linked list
    node8 = SNode(8)
    print("Insert node8 at end ")
    singleLL.insert_at_end(node8)
    # singleLL.print_ll()

    # delete node from the linked list
    print("delete node from the linked list ")
    singleLL.delete(node7)
    singleLL.delete(node6)
    singleLL.delete(node8)
    singleLL.delete(node8)
    # singleLL.print_ll()

    # delete node by location linked list
    print("delete node by location from the linked list ")
    singleLL.delete_loc(3)
    singleLL.print_ll()

    # delete linked list
    # print("delete linked list ")
    # singleLL.delete_linked_list()
    # singleLL.print_ll()

    # length of linked list
    print("length of linked list ")
    print(singleLL.length())

    # search in linked list
    print("search in linked list ")
    print(singleLL.search(node8))

    # get value of nth element in linked list
    print("get value of nth element in linked list ")
    print(singleLL.GetNth(0))

    # reverse linked list
    print("reverse linked list")
    singleLL.reverse()
    singleLL.print_ll()


