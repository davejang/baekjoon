import sys
input = sys.stdin.readline
n, m = map(int,input().split())
num_list = list(map(int,input().split()))
prefix_sum = [0]
for i in range(n):
  if i == 0:
    prefix_sum.append(num_list[i])
  else:
    prefix_sum.append(prefix_sum[i] + num_list[i])
for i in range(m):
  i, j = map(int,input().split())
  if i == j:
    sum = num_list[i-1]
  else:
    sum = prefix_sum[j] - prefix_sum[i-1]
  print(sum)