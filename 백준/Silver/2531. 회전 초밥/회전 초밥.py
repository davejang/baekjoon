import sys

input = sys.stdin.readline
result = 0

n, d, k, c = map(int,input().split())
container = []
for i in range(n):
  container.append(int(input()))

for i in range(n):
  if i+k <= n:
    temp = container[i:i+k]
  else:
    temp = container[0:i+k-n] + container[i:]
  temp.append(c)
  result = max(result,len(set(temp)))

print(result)