import sys

input = sys.stdin.readline
N = int(input())
dp = [0]*501
temp = [0]*501

for i in range(1,N+1):
  for k in range(1,i+1):
    temp[k] = dp[k]
  if i == 1:
    dp[1] = int(input())
  else:
    current_line = list(map(int,input().split()))
    for j in range(1,i+1):
      if j == 1:
        dp[j] = temp[j] + current_line[j-1]
      elif j == i:
        dp[j] = temp[j-1] + current_line[j-1]
      else:
        dp[j] = max(current_line[j-1]+temp[j-1],current_line[j-1]+temp[j])
print(max(dp))