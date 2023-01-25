class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:

                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None

                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:

                if node.left:
                    tmp = node.left
                else:
                    tmp = node.right

                if parent:
                    if node == parent.left:
                        parent.left = tmp
                    else:
                        parent.right = tmp

                else:
                    self.root = tmp
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right

                while successor.left:
                    parent = successor
                    successor = successor.left
                    if successor.key == node.key + 1:
                        break

                node.key = successor.key
                node.data = successor.data

                if successor == parent.left:
                    if successor.right:
                        parent.left = successor.right
                    else:
                        parent.left = None
                else:
                    if successor.right:
                        parent.right = successor.right
                    else:
                        parent.right = None
            return True

        else:
            return False

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
        while q.size():
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            traversal.append(node.data)
        return traversal


def solution(x):
    return 0
