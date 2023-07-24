import heapq

def dijkstra(start):
  q = []
  # 시작 노드를 위한 최단 거리 = 0
  heapq.heappush(q,(0,start))
  distance[start] = 0
  
  while q:
    # heap 자료구조는 최소값이 최상단이므로, heappop으로 가장 최단 거리에 있는 노드 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 최소비용이 아닐 경우 Skip
    if distance[now] < dist:
      continue

    # 연결된 노드 순회
    for i in graph[now]:
      # 연결된 노드의 거리
      cost = dist + i[1]
      # 현재 연결된 노드를 거칠 때 거리가 더 짧을 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

n, d = map(int,input().split())
INF = int(1e9)
# 노드는 거리 1단위로 가정 (고속도로 길이가 50이라면 1부터 50까지의 노드가 있음)
graph = [[] for i in range(d+1)]
distance = [INF] * (d+1)

# 기본 노드 간 연결 거리 1
for i in range(d):
    graph[i].append((i+1, 1))

for i in range(n):
  start, end, length = map(int,input().split())
  if end > d:
    continue
  graph[start].append((end,length))

# 거리 0에서 시작
dijkstra(0)
# 다익스트라 수행 / 0에서 시작하였으므로 0부터 거리 d 까지의 최소거리가 기록됨
print(distance[d])
  