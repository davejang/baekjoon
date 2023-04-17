from itertools import combinations
from collections import Counter

t = int(input())

for i in range(t):
  a = -1
  check = False
  w = str(input())
  k = int(input())
  
  for x in range(k,len(w)+1):
    for y in range(len(w)-x+1):
      if max(list(Counter(w[y:y+x]).values())) == k:
        # print(w[y:y+x])
        a = len(w[y:y+x])
        check = True
        break
    if check == True:
      break
      
  b = -1
  check = False

  for x in range(len(w)+1,k-1,-1):
    for y in range(len(w)-x,-1,-1):
      if max(list(Counter(w[y:y+x]).values())) == k and w[y] == w[y+x-1] and Counter(w[y:y+x])[w[y]] == k:
        # print(w[y:y+x])
        b = len(w[y:y+x])
        check = True
        break
    if check == True:
      break
  if a == -1 or b == -1:
    print(-1)
  else:
    print(a, b)
