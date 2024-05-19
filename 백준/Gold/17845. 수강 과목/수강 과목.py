import sys

input = sys.stdin.readline

n, k = map(int,input().split())
arr = [[0,0]]
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(k):
    cost, time = map(int,input().split())
    arr.append((cost,time))

for i in range(1,k+1):
    for j in range(1,n+1):
        cost = arr[i][0]
        time = arr[i][1]
        
        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(cost + dp[i-1][j-time], dp[i-1][j])
            
print(dp[k][n])