class UnionFind:

    _Prnt = {}
    _Sz = {}
    _st_cnt = 0

    def __init__(self, init_Arr = None):
        self._Prnt = {}
        self._Sz = {}
        self._st_cnt = 0
        if init_Arr:
            for elem in init_Arr:
                self._Prnt[elem] = elem
                self._Sz[elem] = 1
            self._st_cnt = len(init_Arr)

    def make_set(self, elem):
        if self.find(elem) is None:
            self._Prnt[elem] = elem
            self._Sz[elem] = 1
            self._st_cnt += 1

    def find(self, elem):
        try:
            while self._Prnt[elem] is not elem:
                self._Prnt[elem] = self._Prnt[self._Prnt[elem]]
                elem = self._Prnt[elem]
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
            if self._Sz[root1] < self._Sz[root2]:
                root1, root2 = root2, root1
            self._Prnt[root2] = root1
            self._Sz[root1] += self._Sz[root2]
            self._st_cnt -= 1

    def delete(self, elem):
        root = self.find(elem)
        if root:
            if self._Sz[root] == 1:
                del self._Prnt[root]
                del self._Sz[root]
                self._st_cnt -= 1
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
            return self._Sz[self.find(elem)]
        return len(self._Prnt)

    def set_count(self):
        return self._st_cnt

''' Simple Union-Find
def make_set(elem):
    Prnt[elem] = elem
    Sz[elem] = 1

def find(elem):
    while Prnt[elem] is not elem:
        Prnt[elem] = Prnt[Prnt[elem]]
        elem = Prnt[elem]
    return elem

def union(elem1, elem2):
    root1, root2 = find(elem1), find(elem2)
    if root1 is not root2:
        if Sz[root1] < Sz[root2]:
            root1, root2 = root2, root1
        Prnt[root2] = root1
        Sz[root1] += Sz[root2]

Prnt, Sz = {}, {}
'''
