n, m = map(int,input().split())

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        dp[n] = n * factorial(n-1) 
        return dp[n]
      
factorial(n)
      
print((factorial(n)//factorial(n-m)//factorial(m)))      