import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))
p1, p2 = 0, 0
result = 1e9
sum = arr[0]

while True:
  if sum < s:
    p2 += 1
    if p2 == n:
      break
    sum += arr[p2]
  else:  
    sum -= arr[p1]
    result = min(result,p2-p1+1)
    p1 += 1
  

if result == 1e9:
  print(0)
else:
  print(result)