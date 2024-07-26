import sys
import heapq

input = sys.stdin.readline

counter = []
out = []
result = 0
n, k = map(int,input().split())
temp_counter = 1

for i in range(n):
    id, w = map(int,input().split())
    if len(counter) < k:
        heapq.heappush(counter,(w,temp_counter,id))
        temp_counter += 1
    else:
        time, out_counter_id, out_id = heapq.heappop(counter)
        heapq.heappush(out,(time, -out_counter_id, out_id))
        heapq.heappush(counter,(time + w, out_counter_id, id))
        

while counter:
    time, out_counter_id, out_id = heapq.heappop(counter)
    heapq.heappush(out,(time, -out_counter_id, out_id))

for i in range(1,n+1):
    result += i * heapq.heappop(out)[2]

print(result)