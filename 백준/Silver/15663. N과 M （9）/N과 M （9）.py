import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int,input().split())
num = list(map(int,input().rstrip().split()))

comb = list(set(list(permutations(num,m))))
comb.sort()
for c in comb:
  c = list(map(str,c))
  print(' '.join(c))