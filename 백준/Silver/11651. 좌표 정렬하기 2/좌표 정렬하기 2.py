n = int(input())
list = []

for i in range(n):
  x, y = map(int,input().split())
  list.append((y,x))
list.sort()
for i in range(n):
  print(list[i][1],list[i][0])
