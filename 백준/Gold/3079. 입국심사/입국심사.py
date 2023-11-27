import sys

input = sys.stdin.readline

arr = []
stack = []
n, m = map(int,input().split())

for i in range(n):
  arr.append(int(input()))
arr.sort()

start = 0
end = max(arr) * m
result = end

while start <= end:
  mid = (start + end) // 2
  temp = 0
  for a in arr:
    temp += mid // a
    
  if temp >= m:
    result = min(mid,result)
    end = mid - 1
  else:
    start = mid + 1

print(result)