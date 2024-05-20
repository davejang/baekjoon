import sys

input = sys.stdin.readline
INF = int(1e9)

c, n = map(int,input().split())
dp = [INF] * (c + 100)
city = []
dp[0] = 0

for i in range(n):
    expense, customer = map(int,input().split())
    city.append((expense,customer))
    
for expense, customer in city:
    for i in range(customer,c+100):
        dp[i] = min(dp[i-customer] + expense,dp[i])
        
print(min(dp[c:]))