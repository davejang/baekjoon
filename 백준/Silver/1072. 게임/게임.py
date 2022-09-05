X, Y = map(int, input().split())
Z = Y*100 // X
start =0
end = 1000000000
result = 0
while start <= end:
  mid = (start + end) // 2
  if (Y + mid) * 100 // (X + mid) > Z:
    end = mid-1
    result = mid
  else:
    start = mid + 1
if result == 0:
  print(-1)
else:
  print(result)
