import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = []
dp = [0] * (n+1)
for i in range(n):
    num, start, end = map(int,input().split())
    lectures.append((start,end,num))
lectures.sort()
    
q = []
answer = 0

for start, end, num in lectures:
    if q and start >= q[0][0]:
        dp[num] = dp[q[0][2]]
        heapq.heappop(q)
    else:
        answer += 1
        dp[num] = answer
    
    heapq.heappush(q,(end,start,num))
    
print(answer)
for i in dp[1:]:
    print(i)