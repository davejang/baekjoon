import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque([])
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
                
    return result

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
arr = topology_sort()
for i in arr:
    print(i,end=' ')