import sys

input = sys.stdin.readline

n, t = map(int,input().split())
subject = [(0,0)]
dp = [0] * (t + 1)

for i in range(n):
    time, score = map(int,input().split())
    subject.append((time,score))
    
for time, score in subject:
    for i in range(t,time-1,-1):
        dp[i] = max(dp[i],dp[i-time] + score)
    
print(dp[t])