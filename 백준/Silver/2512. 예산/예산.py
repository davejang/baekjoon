import sys

input = sys.stdin.readline
N = int(input())

request = list(map(int,input().split()))
budget = int(input())
request.sort()

start = 0
end = request[N-1]

while start <= end:
  result = 0
  mid = (start + end) // 2
  for i in request:
    result += min(mid,i)
  if result > budget:
    end = mid - 1
  else:
    start = mid + 1

if result > budget:
  print(mid-1)
else:
  print(mid)
      