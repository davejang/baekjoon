import sys

input = sys.stdin.readline

n, h = map(int,input().split())
arr1_count = [0] * (h+1)
arr2_count = [0] * (h+1)

result = n
result_count = 0

for i in range(n):
  height = int(input())
  if i % 2 == 0:
    arr1_count[height] += 1
  else:
    arr2_count[height] += 1

for i in range(h-1,0,-1):
  arr1_count[i] += arr1_count[i+1]
  arr2_count[i] += arr2_count[i+1]

for i in range(1,h+1):
  count = arr1_count[i] + arr2_count[h-i+1]
  if count < result:
    result = count
    result_count = 1
  elif count == result:
    result_count += 1

print(result,result_count)