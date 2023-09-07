import sys

input = sys.stdin.readline
INF = 1e9

n, k = map(int,input().split())
dp = [INF] * (k + 1)
dp[0] = 0

for i in range(n):
  coin = int(input())
  for j in range(coin,k+1):
    dp[j] = min(dp[j],dp[j-coin]+1)

if dp[k] == INF:
  print(-1)
else:
  print(dp[k])