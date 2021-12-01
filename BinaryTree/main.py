from builtins import int

from BinaryTree.BTree import BinaryTree
from BinaryTree.BNode import BNode

if __name__ == '__main__':
    root = BNode(1)
    node2 = BNode(2)
    node3 = BNode(3)
    node4 = BNode(4)
    node5 = BNode(5)
    node6 = BNode(6)
    node7 = BNode(7)
    binaryTree = BinaryTree()
    binaryTree.head = root
    root.left = node2
    node2.left = node4
    node2.right = node5
    root.right = node3
    node3.left = node7
    node3.right = node6
    print("Preorder ")
    # binaryTree.preorder(root)
    print("Inorder ")
    # binaryTree.inorder(root)
    print("postorder ")
    # binaryTree.postorder(root)
    print("Label ")
    # binaryTree.labelWiseTransversal(root)
    # print("Height of a binary tree {}".format(binaryTree.height(root)))

    print("Construct PreOrder Binary Tree ")
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C' , 'F']
    # rootNode = binaryTree.constructPreOrderTree(inOrder, preOrder, 0, len(inOrder) - 1)
    # binaryTree.preorder(rootNode)

    print("Construct PostOrder Binary Tree ")
    In = [4, 8, 2, 5, 1, 6, 3, 7]
    post = [8, 4, 5, 2, 6, 7, 3, 1]
    rootNode = binaryTree.constructPostOrderTree(In, post, 0, len(post) - 1)
    binaryTree.preorder(rootNode)
