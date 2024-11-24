from itertools import product, combinations
from math import sqrt, gcd
from bisect import bisect, bisect_left
from collections import deque, Counter, defaultdict
from sortedcontainers import SortedSet, SortedList
import sys
import sys
import sys #3度目の正直
input = sys.stdin.readline
set = SortedSet
sys.setrecursionlimit(10**8) # 再帰関数の上限の変更

# 入力関連
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LSI(): return list(str(input()))

# 出力関連
def Yes(): print("Yes")
def No(): print("No")
def Ketsugou(l): return "".join(l)

# 定数
def INF(): return 2*(10**18)

# 累積和
def Ruisekiwa(n, **l):
    ans = [0]*n
    for i in range(n):
        if i == 0:
            ans[0]=l[0]
        else:
            ans[i]=ans[i-1]+l[i]
    return ans


#ﾊﾞﾝﾊﾞﾝﾊﾞﾝ
#ﾊﾞﾝﾊﾞﾝﾊﾞﾝﾊﾞﾝﾞﾝ ﾊﾞﾝﾊﾞﾝ
#  （∩`･ω･）ﾊﾞﾝﾊﾞﾝﾊﾞﾝﾊﾞﾝ
#__/_ﾐつ/￣￣￣/
#    \/_____/