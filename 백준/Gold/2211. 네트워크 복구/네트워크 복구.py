import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x):
    q = []
    
    distance[x] = 0
    heapq.heappush(q,(0,x))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for next, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                parent[next] = now
                distance[next] = cost
                heapq.heappush(q,(cost,next))


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
dijkstra(1)
print(n-1)
for i in range(2,n+1):
    print(i,parent[i])