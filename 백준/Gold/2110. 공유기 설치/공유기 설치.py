import sys

input = sys.stdin.readline

arr = []
answer = 0

n, c = map(int,input().split())
for i in range(n):
  arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]

while start <= end:
  mid = (start + end) // 2
  count = 1
  cur = arr[0]
  
  for i in range(1,n):
    if arr[i] - cur >= mid:
      count += 1
      cur = arr[i]

  if count >= c:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)