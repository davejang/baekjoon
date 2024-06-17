import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    result = [0] * (n+1)
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result[now] += time[now]
        
        for next in graph[now]:
            indegree[next] -= 1
            result[next] = max(result[next],result[now])
            if indegree[next] == 0:
                q.append(next) 
                
    return result

n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(n):
    info = list(map(int,input().split()))
    
    time[i+1] = info[0]
    
    for j in range(1,len(info)):
        if info[j] != -1:
            graph[info[j]].append(i+1)
            indegree[i+1] += 1
            
result = topology_sort()
for i in range(1,n+1):
    print(result[i])