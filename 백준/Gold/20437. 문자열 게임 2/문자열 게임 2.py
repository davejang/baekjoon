from collections import defaultdict

t = int(input())

for i in range(t):
  c_count = defaultdict(list)
  w = str(input())
  k = int(input())
    
  for i in range(len(w)):
    if w.count(w[i]) >= k:
        c_count[w[i]].append(i)

  if not c_count:
    print(-1)
    continue

  a = len(w)
  b = 0

  for idx_list in c_count.values():
    for j in range(len(idx_list)-k+1):
        temp = idx_list[j+k-1] - idx_list[j] + 1

        if temp < a:
            a = temp

        if temp > b:
            b  = temp

  print(a, b)