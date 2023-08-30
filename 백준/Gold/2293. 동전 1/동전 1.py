import sys

input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
dp = [0] * (k+1)

for i in range(n):
  coin.append(int(input()))
dp[0] = 1


for i in coin:
  for j in range(1,k+1):
    if i <= j:
      dp[j] += dp[j-i]

print(dp[k])