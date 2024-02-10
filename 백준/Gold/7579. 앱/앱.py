import sys

INF = int(1e9)

input = sys.stdin.readline

n, m = map(int,input().split())

memory_list = [0] + list(map(int,input().rstrip().split()))
cost_list = [0] + list(map(int,input().rstrip().split()))
dp = [[0 for _ in range(sum(cost_list)+1)] for _ in range(n+1)]
result = sum(cost_list) + 1

for i in range(1,n+1):
  memory = memory_list[i]
  cost = cost_list[i]
  for j in range(sum(cost_list)+1):
    if j < cost:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

    if dp[i][j] >= m:
      result = min(result,j)

print(result)