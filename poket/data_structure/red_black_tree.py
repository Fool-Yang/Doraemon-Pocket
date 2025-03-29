# deque used for inorder output
from collections import deque

# left leaning red black tree
class RBTree:

    class Node:

        def __init__(self, key, value = None):
            self.key = key
            self.value = value
            self.is_red = True
            self.left = None
            self.right = None

        def __repr__(self):
            return '{} Key: {} value: {}'.format('Red  ' if self.is_red else 'Black', self.key, self.value)

    def __init__(self):
        self.root = None

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

    def insert(self, key, value = None):
        self.root = self._insert(self.Node(key, value), self.root)
        self.root.is_red = False

    def _insert(self, n, curr):
        if curr:
            if n.key < curr.key:
                curr.left = self._insert(n, curr.left)
            elif curr.key < n.key:
                curr.right = self._insert(n, curr.right)
            else:
                # the key is already in the tree
                # don't insert the same key twice
                # or you mess up the delete
                # update the value instead
                curr.value = n.value
            return self.fix_up(curr)
        return n

    def delete(self, key):
        if self.root:
            if not (self.is_red(self.root.left) or self.is_red(self.root.right)):
                self.root.is_red = True
            self.root = self._delete(key, self.root)
            if self.root:
                self.root.is_red = False

    def _delete(self, key, curr):
        try:
            if key < curr.key:
                if not (self.is_red(curr.left) or self.is_red(curr.left.left)):
                    curr = self.move_red_left(curr)
                curr.left = self._delete(key, curr.left)
            else:
                if self.is_red(curr.left):
                    curr = self.rotate_right(curr)
                if key == curr.key and not curr.right:
                    return None
                if not (self.is_red(curr.right) or self.is_red(curr.right.left)):
                    curr = self.move_red_right(curr)
                if key == curr.key:
                    succ = self._min(curr.right)
                    curr.key, curr.value = succ.key, succ.value
                    curr.right = self._delete_min(curr.right)
                else:
                    curr.right = self._delete(key, curr.right)
        except AttributeError:
            pass
        return self.fix_up(curr)

    def _min(self, curr):
        if curr:
            while curr.left:
                curr = curr.left
        return curr

    def _delete_min(self, curr):
        if curr.left:
            if not (self.is_red(curr.left) or self.is_red(curr.left.left)):
                curr = self.move_red_left(curr)
            curr.left = self._delete_min(curr.left)
            return self.fix_up(curr)
        return None

    def is_red(self, n):
        if n:
            return n.is_red
        return False

    def fix_up(self, n):
        if self.is_red(n.right) and not self.is_red(n.left):
            n = self.rotate_left(n)
        if self.is_red(n.left) and self.is_red(n.left.left):
            n = self.rotate_right(n)
        if self.is_red(n.left) and self.is_red(n.right):
            self.flip_colors(n)
        return n

    def flip_colors(self, n):
        n.left.is_red = not n.left.is_red
        n.right.is_red = not n.right.is_red
        n.is_red = not n.is_red

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        x.is_red = n.is_red
        n.is_red = True
        return x

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        x.is_red = n.is_red
        n.is_red = True
        return x

    def move_red_left(self, n):
        self.flip_colors(n)
        if self.is_red(n.right.left):
            n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
            self.flip_colors(n)
        return n

    def move_red_right(self, n):
        self.flip_colors(n)
        if self.is_red(n.left.left):
            n = self.rotate_right(n)
            self.flip_colors(n)
        return n

    def __iter__(self):
        return iter(self.inorder())

    def inorder(self):
        Q = deque()
        self._inorder(self.root, Q)
        return Q

    def _inorder(self, n, Q):
        if n:
            self._inorder(n.left, Q)
            Q.append(n)
            self._inorder(n.right, Q)
'''
# test
from random import shuffle
m = 15
for _ in range(10000):
    ran = list(range(m))
    shuffle(ran)
    order = []
    t = RBTree()
    for k in ran:
        order.append(k)
        order.sort()
        t.insert(k)
        t_order = [n.key for n in t.inorder()]
        if order != t_order:
            print(k, order, t_order)
            break
    ran += list(range(m, m + m))
    shuffle(ran)
    for k in ran:
        try:
            order.remove(k)
        except ValueError:
            pass
        t.delete(k)
        t_order = [n.key for n in t.inorder()]
        if order != t_order:
            print(k, order, t_order)
            break
'''
