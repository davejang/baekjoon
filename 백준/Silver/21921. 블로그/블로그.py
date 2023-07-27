import sys

input = sys.stdin.readline

n, x = map(int,input().split())
visitor = list(map(int,input().rstrip().split()))
max = 0
count = 0
prefix_sum = [0] * (n+1)
prefix_sum[0] = 0

for i in range(1,n+1):
  prefix_sum[i] = prefix_sum[i-1] + visitor[i-1]

i = 0
while i+x <= n:
  if prefix_sum[i+x] - prefix_sum[i] > max:
    max = prefix_sum[i+x] - prefix_sum[i]
    count = 1
  elif prefix_sum[i+x] - prefix_sum[i] == max:
    count += 1

  i+=1

if max == 0:
  print('SAD')
else:
  print(max)
  print(count)