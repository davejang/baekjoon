import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    q = deque()
    result = []
    
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
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    arr = list(map(int,input().split()))
    for j in range(1,len(arr)-1):
        graph[arr[j]].append(arr[j+1])
        indegree[arr[j+1]] += 1
        
result = topology_sort()
if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)