import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x):
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q,(0,x))
    distance[x] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        
        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
                
    return distance

n = int(input())
graph = [[] for _ in range(n+1)]
candidate = list(map(int,input().split()))
m = int(input())

for i in range(m):
    d, e, l = map(int,input().split())
    graph[d].append((e,l))
    graph[e].append((d,l))


max_length = 0
answer = 0
dist_a = dijkstra(candidate[0])
dist_b = dijkstra(candidate[1])
dist_c = dijkstra(candidate[2])

for i in range(1,n+1):
    if max_length < min(dist_a[i], dist_b[i], dist_c[i]):
        max_length = min(dist_a[i], dist_b[i], dist_c[i])
        answer = i
print(answer)