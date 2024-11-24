from collections import defaultdict, deque

class TsuchanList:
    def __init__(self, l: list):
        self.list = defaultdict(int)
        self.where = defaultdict(deque)
        self.l = 0
        self.r = 0
        for i in l:
            self.add(i)
            #print(self.list)
    
    def add(self, n):
        self.list[self.r] += n
        self.where[n].append(self.r)     
        self.r += 1
    
    def addleft(self, n):
        self.l -= 1
        self.list[self.l] += n
        if not n in self.where:
            self.where[n] = deque([])
        self.where[n].appendleft(self.l)
    
    def pop(self):
        self.where[self.list[self.r-1]].pop()
        if len(self.where[self.list[self.r-1]]) == 0:
            del self.where[self.list[self.r-1]]
        self.list[self.r] = 0
        self.r = self.r-1

    def popleft(self):
        self.where[self.list[self.l]].popleft()
        if len(self.where[self.list[self.l]]) == 0:
            del self.where[self.list[self.l]]
        self.list[self.l] = 0
        self.l = self.l+1

    def index(self, i):
        return self.where[i][0]-self.l
    
    def __str__(self):
        l = []
        for i in range(self.l, self.r):
            l.append(self.list[i])
        return "TsuchanList" + str(l)

    def __iter__(self):
        for i in range(self.l, self.r):
            yield self.list(i)

    def __len__(self):
        return self.r-self.l
    
    def __getitem__(self, i: int):
        if not 0 <= i <= self.r-self.l:
            raise IndexError
        return self.list[self.l+i]
    
    def __contains__(self, n):
        try:
            if len(self.where[n]):
                return True
        except:
            return False

if __name__ == "__main__":
    a  = TsuchanList([1, 4, 3, 5, 8])
    a.pop()
    if 4 in a:
        print(a)
    a.popleft()
    if 1 in a:
        print(a)
    print(a)