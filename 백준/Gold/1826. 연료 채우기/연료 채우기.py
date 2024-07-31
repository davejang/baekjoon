import sys
import heapq

input = sys.stdin.readline

q = []
gas_station = []
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    gas_station.append((a,b))
gas_station.sort(key=lambda x:x[0])
# l 마을위치 p 현재 연료
l, p = map(int,input().split())
gas_station.append((l,0))

current_position = 0
current_fuel = p
result = 0

for a, b in gas_station:
    # 현재 연료가 최종 목적지 위치보다 많을 경우
    if current_fuel >= l - current_position:
        break
    
    # 현재 위치에서 이전 주유소들의 연료로 도달할 수 있는지 계산
    while a > current_fuel and q:
        fuel = heapq.heappop(q)
        current_fuel += -fuel
        result += 1
    # 이전 주유소들의 연료로 도달하지 못할 경우 break
    if a > current_fuel:
        break
    
    heapq.heappush(q,-b)

if current_fuel < l:
    print(-1)
else:
    print(result)