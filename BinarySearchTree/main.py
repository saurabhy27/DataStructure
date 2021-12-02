from BinarySearchTree.BTree import BinarySearchTree
from BinarySearchTree.BNode import BNode

if __name__ == '__main__':
    #             5
    #     2               8
    # 1       3       7       9
    #             4               10

    node1 = BNode(1)
    node2 = BNode(2)
    node3 = BNode(3)
    node4 = BNode(4)
    node5 = BNode(5)
    node7 = BNode(7)
    node8 = BNode(8)
    node9 = BNode(9)
    node10 = BNode(10)
    root = node5
    binarySearchTree = BinarySearchTree()
    binarySearchTree.head = root
    root.left = node2
    node2.left = node1
    node2.right = node3
    node3.right = node4

    root.right = node8
    node8.left = node7
    node8.right = node9
    node9.right = node10
    print("Preorder ")
    # binarySearchTree.preorder(root)
    print("Inorder ")
    # binarySearchTree.inorder(root)
    print("postorder ")
    # binarySearchTree.postorder(root)
    print("Label ")
    # binarySearchTree.labelWiseTransversal(root)
    print("Search ")
    # print(binarySearchTree.search(root, 100))
    # print(binarySearchTree.searchRecursively(root, 10))
    print("Smallest and Largest ket ")
    # print(binarySearchTree.smallestAndLargestKey(root))
    print("Insert a new node ")
    # node6 = BNode(6)
    # root = binarySearchTree.insert(root, node6)
    # binarySearchTree.labelWiseTransversal(root)
    print("Delete a Node ")
    root = binarySearchTree.delete(root, node2.data)
    binarySearchTree.labelWiseTransversal(root)
