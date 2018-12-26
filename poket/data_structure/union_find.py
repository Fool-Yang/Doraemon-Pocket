class UnionFind:

    Parent = {}
    Sz = {}
    set_cnt = 0

    def __init__(self, init_Arr = None):
        self.Parent = {}
        self.Sz = {}
        self.set_cnt = 0
        if init_Arr:
            for elem in init_Arr:
                self.Parent[elem] = elem
                self.Sz[elem] = 1
            self.set_cnt = len(init_Arr)

    def make_set(self, elem):
        if self.find(elem) is None:
            self.Parent[elem] = elem
            self.Sz[elem] = 1
            self.set_cnt += 1

    def find(self, elem):
        try:
            while self.Parent[elem] is not elem:
                self.Parent[elem] = self.Parent[self.Parent[elem]]
                elem = self.Parent[elem]
            return elem
        except KeyError:
            return None

    def union(self, elem1, elem2):
        root1, root2 = self.find(elem1), self.find(elem2)
        if root1 is None:
            self.make_set(elem1)
            root1 = elem1
        if root2 is None:
            self.make_set(elem2)
            root2 = elem2
        if root1 is not root2:
            if self.Sz[root1] < self.Sz[root2]:
                root1, root2 = root2, root1
            self.Parent[root2] = root1
            self.Sz[root1] += self.Sz[root2]
            self.set_cnt -= 1

    def delete(self, elem):
        root = self.find(elem)
        if root:
            if self.Sz[root] == 1:
                del self.Parent[root]
                del self.Sz[root]
                self.set_cnt -= 1
            else:
                raise AssertionError('not supported')

    def remove(self, elem):
        self.delete(elem)

    def move(self, elem1, elem2):
        root1, root2 = self.find(elem1), self.find(elem2)
        if root1 is not root2:
            self.delete(elem1)
            self.make_set(elem1)
            self.union(elem1, elem2)

    def size(self, elem = None):
        if elem:
            return self.Sz[self.find(elem)]
        return len(self.Parent)

    def set_count(self):
        return self.set_cnt

''' Simple Union-Find
def make_set(elem):
    Parent[elem] = elem
    Sz[elem] = 1

def find(elem):
    while Parent[elem] is not elem:
        Parent[elem] = Parent[Parent[elem]]
        elem = Parent[elem]
    return elem

def union(elem1, elem2):
    root1, root2 = find(elem1), find(elem2)
    if root1 is not root2:
        if Sz[root1] < Sz[root2]:
            root1, root2 = root2, root1
        Parent[root2] = root1
        Sz[root1] += Sz[root2]

Parent, Sz = {}, {}
'''
