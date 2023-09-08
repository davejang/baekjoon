import sys

input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
graph  = [list(map(int,input().rstrip().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):

    if dp[i][j] == 0 or graph[i][j] == 0:
      continue
      
    cost = graph[i][j]
    if i + cost < n:
      dp[i+cost][j] += dp[i][j]

    if j + cost < n:
      dp[i][j+cost] += dp[i][j]

print(dp[-1][-1])