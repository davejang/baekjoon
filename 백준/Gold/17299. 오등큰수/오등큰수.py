import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)
stack = []
answer = [-1 for _ in range(n)]
arr = list(map(int,input().rstrip().split()))

for i in arr:
  dict[i] += 1

for i in range(n):
  while stack and dict[arr[stack[-1]]] < dict[arr[i]]:
    answer[stack.pop()] = arr[i]
  stack.append(i)

print(*answer)