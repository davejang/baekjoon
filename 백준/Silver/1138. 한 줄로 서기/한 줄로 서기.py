import sys

input = sys.stdin.readline

n = int(input())
memory = list(map(int,input().rstrip().split()))
arr = [0] * (n)

for i in range(n):
  left = memory[i]
  count = 0
  for j in range(n):
    if arr[j] != 0:
      continue
    count += 1
    if count == left + 1:
      arr[j] = str(i+1)
      break
  
print(' '.join(arr))