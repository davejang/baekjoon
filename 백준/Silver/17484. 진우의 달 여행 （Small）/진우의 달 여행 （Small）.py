import sys

input = sys.stdin.readline

n, m = map(int,input().split())
INF = int(1e9)
result = INF

space = []
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]
for i in range(n):
  space.append(list(map(int,input().rstrip().split())))

# 첫째라인 init
for j in range(m):
  for k in range(3):
    dp[0][j][k] = space[0][j]

for i in range(1,n):
  for j in range(m):
    for k in range(3):
      if (j == 0 and k == 0) or (j == m - 1 and k == 2):
        continue
      # 왼쪽
      if k == 0:
          dp[i][j][k] = space[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
      # 중간
      if k == 1:
          dp[i][j][k] = space[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
      # 오른쪽
      if k == 2:
          dp[i][j][k] = space[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

for i in range(m):
  result = min(result,min(dp[-1][i]))
print(result)