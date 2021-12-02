class BinarySearchTree:
    def preorder(self, root):
        if root is None:
            return
        print("Data value {}".format(root.data))
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print("Data value {}".format(root.data))
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print("Data value {}".format(root.data))

    def labelWiseTransversal(self, root):
        if root is None:
            return
        queue = [root]
        resp = []
        while len(queue) > 0:
            removedNode = queue.pop(0)
            resp.append(removedNode.data)
            if removedNode.left is not None:
                queue.append(removedNode.left)
            if removedNode.right is not None:
                queue.append(removedNode.right)
        print(resp)

    def search(self, root, value):
        if root is None:
            return False
        queue = [root]
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if removedNode.data == value:
                return True
            if removedNode.left is not None:
                if removedNode.data > value:
                    queue.append(removedNode.left)
            if removedNode.right is not None:
                if removedNode.data < value:
                    queue.append(removedNode.right)
        return False

    def searchRecursively(self, root, param):
        if root is None:
            return False
        if root.data == param:
            return True
        if root.data > param:
            return self.searchRecursively(root.left, param)
        return self.searchRecursively(root.right, param)

    def smallestAndLargestKey(self, root):
        if root is None:
            return None
        queue = [root]
        smallestKeyValue = largestKeyValue = root.data
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if smallestKeyValue >= removedNode.data:
                smallestKeyValue = removedNode.data
            if largestKeyValue <= removedNode.data:
                largestKeyValue = removedNode.data
            if removedNode.left is not None:
                queue.append(removedNode.left)
            if removedNode.right is not None:
                queue.append(removedNode.right)
        return smallestKeyValue, largestKeyValue

    def insert(self, root, node):
        if root is None:
            return False
        queue = [root]
        while len(queue) > 0:
            removedNode = queue.pop(0)
            if removedNode.data == node.data:
                return False
            if removedNode.left is not None:
                if removedNode.data > node.data:
                    queue.append(removedNode.left)
            else:
                removedNode.left = node
                break
            if removedNode.right is not None:
                if removedNode.data < node.data:
                    queue.append(removedNode.right)
            else:
                removedNode.right = node
                break
        return root

    def delete(self, root, deletedNodeKey):
        if not root:
            return root
        elif root.data > deletedNodeKey:
            root.left = self.delete(root.left, deletedNodeKey)
        elif root.data < deletedNodeKey:
            root.right = self.delete(root.right, deletedNodeKey)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                tmp = self.finMinRightTreeCount(root.right)
                root.data = tmp.data
                root.right = self.delete(root.right, tmp.data)
        return root

    def finMinRightTreeCount(self, root):
        current = root
        while current.left:
            current = current.left
        return current
