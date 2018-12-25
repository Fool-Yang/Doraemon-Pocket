from collections import deque
class RBTree: 

    root = None

    def __init__(self, key = None, value = None):
        if key:
            self.root = Node(key, value)

    def search(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr
        return None

    def min(self):
        return self._min(self.root)

    def _min(self, curr):
        if curr:
            while curr.left:
                curr = curr.left
        return curr

    def max(self):
        return self._max(self.root)

    def _max(self, curr):
        if curr:
            while curr.right:
                curr = curr.right
        return curr

    def insert(self, key, value = None):
        n = Node(key, value)
        self.root = self._insert(n, self.root)
        self.root.is_red = False

    def add(self, key, value = None):
        self.insert(key, value)

    def _insert(self, n, curr):
        if curr:
            if n.key <= curr.key:
                curr.left = self._insert(n, curr.left)
            else:
                curr.right = self._insert(n, curr.right)
            return self.FixUp(curr)
        return n

    def delete(self, key):
        self.root = self._delete(key, self.root)
        if self.root:
            self.root.is_red = False

    def remove(self, key):
        self.delete(key)

    def _delete(self, key, curr):
        try:
            if key < curr.key:
                if not (self.is_red(curr.left) or self.is_red(curr.left.left)):
                    curr = self.MoveRedLeft(curr)
                curr.left = self._delete(key, curr.left)
            else:
                if self.is_red(curr.left):
                    curr = self.RotateRight(curr)
                if key == curr.key and not curr.right:
                    return None
                if not (self.is_red(curr.right) or self.is_red(curr.right.left)):
                    curr = self.MoveRedRight(curr)
                if key == curr.key:
                    succ = self._min(curr.right)
                    curr.key, curr.value = succ.key, succ.value
                    curr.right = self.DeleteMin(curr.right)
                else:
                    curr.right = self._delete(key, curr.right)
        except AttributeError:
            pass
        return self.FixUp(curr)

    def DeleteMin(self):
        self.root = _DeleteMin(self.root)
        self.root.is_red = False

    def RemoveMin(self):
        self.DeleteMin()

    def _DeleteMin(self, curr):
        if curr.left:
            if not (self.is_red(curr.left) or self.is_red(curr.left.left)):
                curr = self.MoveRedLeft(curr)
            curr.left = _DeleteMin(curr.left)
            return FixUp(curr)
        return None

    def DeleteMax(self):
        self.root = self._DeleteMax(self.root)
        self.root.is_red = False

    def RemoveMax(self):
        self.DeleteMax()

    def _DeleteMax(self, curr):
        return

    def MoveRedLeft(self, n):
        self.FlipColors(n)
        if self.is_red(n.right.left):
            n.right = self.RotateRight(n.right)
            n = self.RotateLeft(n)
            self.FlipColors(n)
        return n

    def MoveRedRight(self, n):
        self.FlipColors(n)
        if self.is_red(n.left.left):
            n = self.RotateRight(n)
            self.FlipColors(n)
        return n

    def is_red(self, n):
        if n:
            return n.is_red
        return False

    def FixUp(self, n):
        if self.is_red(n.right) and not self.is_red(n.left):
            n = self.RotateLeft(n)
        if self.is_red(n.left) and self.is_red(n.left.left):
            n = self.RotateRight(n)
        if self.is_red(n.left) and self.is_red(n.right):
            self.FlipColors(n)
        return n

    def FlipColors(self, n):
        n.left.is_red = not n.left.is_red
        n.right.is_red = not n.right.is_red
        n.is_red = not n.is_red

    def RotateLeft(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        x.is_red = n.is_red
        n.is_red = True
        return x

    def RotateRight(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        x.is_red = n.is_red
        n.is_red = True
        return x

    def __iter__(self):
        return iter(self.InOrder())

    def InOrder(self):
        Q = deque()
        self._InOrder(self.root, Q)
        return Q

    def _InOrder(self, n, Q):
        if n:
            self._InOrder(n.left, Q)
            Q.append(n)
            self._InOrder(n.right, Q)

class Node:

    key = None
    value = None
    left = None
    right = None
    is_red = True

    def __init__(self, key, value = None):
        self.key = key
        self.value = value

    def __repr__(self):
        return '{} Key: {} value: {}'.format('Red  ' if self.is_red else 'Black', self.key, self.value)
