from itertools import combinations

n, m = map(int,input().split())
s = ''
for i in range(1,n+1):
  s += str(i)
arr = list(combinations(s,m))

for i in range(len(arr)):
  for j in range(len(arr[i])):
    if j == m - 1:
      print(int(arr[i][j]), sep = '/n')
    else:
      print(int(arr[i][j]), end = ' ')