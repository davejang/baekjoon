import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            cost[i] += time[i-1]
            
    while q:
        now = q.popleft()
        result.append(now)
        
        for next in graph[now]:
            indegree[next] -= 1
            cost[next] = max(cost[now] + time[next-1], cost[next])
            if indegree[next] == 0:
                q.append(next)

    return cost

t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    time = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    cost = [0] * (n+1)
    
    for _ in range(k):
        x, y = map(int,input().split())
        graph[x].append(y)
        indegree[y] += 1
        
    w = int(input())
    topology_sort()
    print(cost[w])