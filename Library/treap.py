import random
class Node:
    def __init__(self, data):
        self.data = data
        self.count = 1  # 重複数
        self.cnt = 1    # 部分木サイズ
        self.priority = random.random()
        self.left = None
        self.right = None
def cnt(node): return node.cnt if node else 0
def upd_cnt(node):
    if node: node.cnt = node.count + cnt(node.left) + cnt(node.right)
class Treap:
    def __init__(self, l=[], MultiSet=False):
        self.root = None
        self.size = 0
        self.multiset = MultiSet
        [self.add(i) for i in l]
    def rotate_right(self, node):
        l = node.left
        node.left = l.right
        l.right = node
        upd_cnt(node)
        upd_cnt(l)
        return l
    def rotate_left(self, node):
        r = node.right
        node.right = r.left
        r.left = node
        upd_cnt(node)
        upd_cnt(r)
        return r
    def add(self, x):
        self.root, added = self._add(self.root, x)
        self.size += 1 if added else 0
    def _add(self, node, x):
        if not node: return Node(x), True
        if x == node.data:
            if self.multiset:
                node.count += 1
                upd_cnt(node)
                return node, True
            else: return node, False
        elif x < node.data:
            node.left, added = self._add(node.left, x)
            if node.left.priority < node.priority: node = self.rotate_right(node)
        else:
            node.right, added = self._add(node.right, x)
            if node.right.priority < node.priority: node = self.rotate_left(node)
        upd_cnt(node)
        return node, added
    def discard(self, x):
        self.root, removed = self._discard(self.root, x)
        if removed: self.size -= 1
    def _discard(self, node, x):
        if not node: return None, False
        if x < node.data: node.left, removed = self._discard(node.left, x)
        elif x > node.data: node.right, removed = self._discard(node.right, x)
        else:
            if node.count > 1:
                node.count -= 1
                upd_cnt(node)
                return node, True
            # 削除処理（片方または両方あり）
            if not node.left: return node.right, True
            if not node.right: return node.left, True
            if node.left.priority < node.right.priority:
                node = self.rotate_right(node)
                node.right, _ = self._discard(node.right, x)
            else:
                node = self.rotate_left(node)
                node.left, _ = self._discard(node.left, x)
            removed = True
        upd_cnt(node)
        return node, removed
    def pop(self, x):
        if x < 0: x += len(self)
        if 0 <= x < len(self): self.discard(self[x])
    def count(self, x):
        node = self.root
        while node:
            if x == node.data: return node.count
            elif x < node.data: node = node.left
            else: node = node.right
        return 0
    def __contains__(self, x): return self.count(x) > 0
    def __len__(self): return self.size
    def __getitem__(self, index):
        if index < 0: index += self.size
        if index < 0 or index >= self.size: raise IndexError("Index out of bounds")
        return self._get_by_index(self.root, index)
    def _get_by_index(self, node, index):
        left_size = cnt(node.left)
        if index < left_size: return self._get_by_index(node.left, index)
        elif index < left_size + node.count: return node.data
        else: return self._get_by_index(node.right, index - left_size - node.count)
    def index(self, x):
        node = self.root
        idx = 0
        while node: 
            if x == node.data: return idx + cnt(node.left)
            elif x < node.data: node = node.left
            else:
                idx += cnt(node.left) + node.count
                node = node.right
        return None
    def lower_bound(self, x):
        node = self.root
        idx = 0
        res = None
        while node:
            if node.data >= x:
                res = idx + cnt(node.left)
                node = node.left
            else:
                idx += cnt(node.left) + node.count
                node = node.right
        return res if res is not None else self.size
    def upper_bound(self, x):
        node = self.root
        idx = 0
        res = None
        while node:
            if node.data > x:
                res = idx + cnt(node.left)
                node = node.left
            else:
                idx += cnt(node.left) + node.count
                node = node.right
        return res if res is not None else self.size
    def __str__(self): return f"Treap[{', '.join(str(self[i]) for i in range(self.size))}]"
