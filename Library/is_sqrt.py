from bisect import bisect_left

class SquareRoot(object):
    def __init__(self, n):
        self.n = n
    def __getitem__(self, index):
        return index * index
    def __len__(self):
        return self.n

def try_square_root(n2):
    n = bisect_left(SquareRoot(n2), n2)
    return n if n*n == n2 else None