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
        self.postorder(node.left)
        self.postorder(node.right)
        print("Data value {}".format(node.data))

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

    def insertFirstInLNRPos(self, root, node):
        if root is None:
            return
        if root.left is None and root.right is not None:
            root.left = node
            print("Left Node Not available {}")
        if root.right is None and root.left is not None:
            root.right = node
            print("Left Node Not available {}")
        self.insertFirstInLNRPos(root.left, node)
        print("Node Data {} ".format(root.data))
        self.insertFirstInLNRPos(root.right, node)

    def insertFirstEmptyPos(self, root, node8):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if removedNode.left is not None:
                queue.append(removedNode.left)
            else:
                removedNode.left = node8
                break
            if removedNode.right is not None:
                queue.append(removedNode.right)
            else:
                removedNode.right = node8
                break
        return root

    def searchNodeValue(self, root, value):
        if root is None:
            return False
        if root.data == value:
            return True
        res = self.searchNodeValue(root.left, value)
        if res:
            return True
        res = self.searchNodeValue(root.right, value)
        return res

    def maxKeyValue(self, root, maxValue):
        if root is None:
            return
        if maxValue[0] <= root.data:
            maxValue[0] = root.data
        self.maxKeyValue(root.left, maxValue)
        self.maxKeyValue(root.right, maxValue)

    def deleteNode(self, root, node):
        if root is None:
            return None
        queue = [root]
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if removedNode is node:
                removedNode = None
                return
            if removedNode.left is not None:
                if removedNode.left == node:
                    removedNode.left = None
                    return
                queue.append(removedNode.left)
            if removedNode.right is not None:
                if removedNode.right == node:
                    removedNode.right = None
                    return
                queue.append(removedNode.right)
        return

    def findDeepestNodeAndKeyNodeAndDelete(self, root, key):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == key:
                return None
            else:
                return root
        queue = [root]
        keyNode = None
        removedNode = None
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if removedNode.data == key:
                keyNode = removedNode
            if removedNode.left is not None:
                queue.append(removedNode.left)
            if removedNode.right is not None:
                queue.append(removedNode.right)
        if keyNode:
            x = removedNode.data
            self.deleteNode(root, removedNode)
            keyNode.data = x
        return root
