import sys
from collections import deque

def topology_sort():
    q = deque([])
    basic = []
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            basic.append(i)
            
    while q:
        now = q.popleft()
        
        for next, need in graph[now]:
            if now in basic:
                dp[next][now] += need
            else:
                for i in range(1,n+1):
                    dp[next][i] += dp[now][i] * need
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    return basic

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    x, y, k = map(int,input().split())
    graph[y].append((x,k))
    indegree[x] += 1
    
basic = topology_sort()

for i in basic:
    print(i,dp[n][i])