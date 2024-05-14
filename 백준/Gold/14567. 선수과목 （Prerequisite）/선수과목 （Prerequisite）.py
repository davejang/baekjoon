import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
indegree = [0] * (n+1)
answer = [1] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
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
                answer[next] = answer[now] + 1

    return result

topology_sort()
for i in range(1,n+1):
    print(answer[i],end=" ")