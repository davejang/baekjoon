import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x, y = map(int,input().split())

graph = [[] for _ in range(n)]
distance = [INF] * n

for i in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))
    
def dijkstra(n):
    q = []
    heapq.heappush(q,(0,n))
    distance[n] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for c in graph[now]:
            cost = dist + c[1]
            if cost < distance[c[0]]:
                distance[c[0]] = cost
                heapq.heappush(q,(cost,c[0]))
    
dijkstra(y)
distance.sort()
temp = 0
result = 1
if max(distance) * 2 > x:
    print(-1)
else:
    for i in range(1,n):
        if (temp + distance[i]) * 2 <= x:
            temp += distance[i]
        else:
            temp = distance[i]
            result += 1  
    print(result)