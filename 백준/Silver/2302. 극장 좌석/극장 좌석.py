import sys

input = sys.stdin.readline

result = 1
temp = 0
n = int(input())
m = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
  dp[i] = dp[i-1] + dp[i-2]

if m > 0:
  for i in range(m):
    vip = int(input())
    if (vip - temp - 1) > 0:
      result = result * dp[vip - temp - 1]
    temp = vip
  print(result * dp[n - temp])
else:
  print(dp[n])