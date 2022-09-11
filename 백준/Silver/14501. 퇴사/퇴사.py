n = int(input())
array = []
dp = [0]*(n+1)
for i in range(n):
  a, b = map(int,input().split())
  array.append((a,b))
for i in range(n-1,-1,-1):
  if i + array[i][0] > n:
    dp[i] = dp[i+1]
  else:
    dp[i] = max(dp[i+1],array[i][1]+dp[i+array[i][0]])
print(dp[0])
