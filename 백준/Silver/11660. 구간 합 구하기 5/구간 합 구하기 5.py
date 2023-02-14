import sys

input = sys.stdin.readline

n, m = map(int,input().split())

arr = []
dp = [[0 for col in range(n + 1)] for row in range(n + 1)]

for i in range(n):
  arr.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(m):
  point = list(map(int,input().split()))
  x1 = point[0] - 1
  y1 = point[1] - 1
  x2 = point[2] - 1
  y2 = point[3] - 1
  print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
  