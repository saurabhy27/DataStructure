from BinaryTree.BNode import BNode


class BinaryTree:
    index = 7

    def __init__(self):
        self.head = None

    def preorder(self, node):
        if node is None:
            return
        print("Data value {}".format(node.data))
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print("Data value {}".format(node.data))
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.right)
        print("Data value {}".format(node.data))
        self.postorder(node.left)

    def labelWiseTransversal(self, node):
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            removedNode = queue.__getitem__(0)
            queue.pop(0)
            if removedNode.left is not None:
                queue.append(removedNode.left)
            if removedNode.right is not None:
                queue.append(removedNode.right)
            print("Data value {}".format(removedNode.data))

    def height(self, root):
        if root is None:
            return 0
        lHeight = self.height(root.left)
        rHeight = self.height(root.right)
        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1

    def setIndex(self):
        self.index += 1

    def constructPreOrderTree(self, inOrder, preOrder, start, end):
        if start > end:
            return None

        node = BNode(preOrder.__getitem__(self.index))
        self.index += 1

        if start == end:
            return node

        inOrderIndex = self.indexSearch(inOrder, start, end, node.data)
        node.left = self.constructPreOrderTree(inOrder, preOrder, start, inOrderIndex - 1)
        node.right = self.constructPreOrderTree(inOrder, preOrder, inOrderIndex + 1, end)
        return node

    def indexSearch(self, inOrder, start, end, data):
        i = 0
        for i in range(start, end + 1):
            if data == inOrder.__getitem__(i):
                break
        return i

    def constructPostOrderTree(self, InOrder, postOrder, start, end):
        if start > end:
            return None
        node = BNode(postOrder.__getitem__(self.index))
        self.index -= 1
        if start == end:
            return node
        inOrderIndex = self.indexSearch(InOrder, start, end, node.data)
        node.right = self.constructPostOrderTree(InOrder, postOrder, inOrderIndex + 1, end)
        node.left = self.constructPostOrderTree(InOrder, postOrder, start, inOrderIndex - 1)
        return node


