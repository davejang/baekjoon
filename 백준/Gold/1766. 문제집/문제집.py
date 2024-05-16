import sys
import heapq
from collections import deque

input = sys.stdin.readline

def topology_sort():
    result = []
    q = []
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(q,(i,0))
            
    while q:
        now, step = heapq.heappop(q)
        result.append(now)
        
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(q,(next,now + 1))
                
    return result
    
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
answer = topology_sort()
for a in answer:
    print(a,end=' ')