import sys

input = sys.stdin.readline

n, k = map(int,input().split())
stuff = []
for i in range(n):
  w, v = map(int,input().split())
  stuff.append((w,v))

dp = [0] * (k+1)

for weight, value in stuff:
  for i in range(k,weight-1,-1):
    dp[i] = max(dp[i],dp[i-weight] + value)

print(dp[k])