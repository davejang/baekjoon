import sys

input = sys.stdin.readline

d, p = map(int,input().split())
dp = [0] * (d+1)
dp[0] = int(1e9)
pipe = []

for i in range(p):
    l, c = map(int,input().split())
    pipe.append((l,c))
    
for length, volumn in pipe:
    for i in range(d,length-1,-1):
        if i == length:
            dp[i] = max(dp[i], volumn)
        else:
            dp[i] = max(dp[i], min(dp[i-length], volumn))
        
print(dp[-1]) 