class UnionFind:
    def __init__(self, n):
        self._n = n
        self.points = [-1]*n
    def find(self, a):
        assert 0 <= a < self._n
        if self.points[a] < 0: 
            return a
        self.points[a] = self.find(self.points[a])
        return self.points[a]
    def union(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.find(a), self.find(b)
        if x == y: return x
        if self.points[x] > self.points[y]:
            x, y = y, x
        self.points[x] += self.points[y]
        self.points[y] = x
        return x
    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.find(a) == self.find(b)
    def size(self, a):
        assert 0 <= a < self._n
        return -self.points[self.union(a)]
    def groups(self):
        leader_buf = [self.find(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)
        return [r for r in result if r != []]