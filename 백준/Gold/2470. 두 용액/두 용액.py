import sys

input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))
array.sort()
start = 0
end = n - 1
sum = abs(array[start] + array[end])
r1 = array[0]
r2 = array[end]

while start < end:
  if abs(array[start] + array[end]) < sum:
    sum = abs(array[start] + array[end])
    r1 = array[start]
    r2 = array[end]
  if array[start] + array[end] > 0:
    end = end - 1
  else:
    start = start + 1

print(r1,r2)