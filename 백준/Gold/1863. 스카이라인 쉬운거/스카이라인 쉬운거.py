import sys

input = sys.stdin.readline
stack = []
result = 0

n = int(input())
for i in range(n):
  x, y = map(int,input().split())

  while stack:
    if stack[-1] > y:
      stack.pop()
      result += 1
    else:
      break

  if y == 0:
    continue

  if stack:
    if stack[-1] == y:
      continue

  stack.append(y)

print(result + len(stack))