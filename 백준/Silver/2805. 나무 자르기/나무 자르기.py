n, m = map(int,input().split())
wood = list(map(int,input().split()))

start = 0
end = max(wood)

while start <= end:
  mid = (start + end) // 2
  length = 0
  for i in wood:
    if mid < i:
      length = length + (i - mid)
    if length >= m:
      break
  if length >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)