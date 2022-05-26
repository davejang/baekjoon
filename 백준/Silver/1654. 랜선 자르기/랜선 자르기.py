k, n = map(int,input().split())
line = []
for i in range(k):
  line.append(int(input()))
line.sort()

end = max(line)
start = 1
count = 0
result = 0

while start <= end:
  mid = (start + end) // 2
  count = 0
  for i in range(k):
    count = count + (line[i] // mid)
  if count < n:
    end = mid - 1
  elif count >= n:
    start = mid + 1
    
print(end)