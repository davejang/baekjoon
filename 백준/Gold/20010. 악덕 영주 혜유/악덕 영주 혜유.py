import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
def dijkstra(a):
    distance = [INF for _ in range(n)]
    q = []
    heapq.heappush(q,(0,a))
    distance[a] = 0
    
    while q:
        cost, now = heapq.heappop(q)
        
        if cost > distance[now]:
            continue
        
        for next in graph[now]:
            next_cost = next[1] + cost
            if next_cost < distance[next[0]]:
                heapq.heappush(q,(next_cost,next[0]))
                distance[next[0]] = next_cost
                
    return max(distance)
    
n, k = map(int,input().split())
parents = [i for i in range(n)]
graph = [[] for _ in range(n)]
edges = []
min_cost = 0
max_cost = 0

for i in range(k):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        min_cost += cost
        graph[a].append((b,cost))
        graph[b].append((a,cost))
        
for i in range(n):
    max_cost = max(max_cost,dijkstra(i))
    
        
print(min_cost)
print(max_cost)