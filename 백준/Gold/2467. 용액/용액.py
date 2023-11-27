import sys

input = sys.stdin.readline

min_val = float("INF")

n = int(input())
arr = list(map(int,input().rstrip().split()))
ans_a = arr[0]
ans_b = arr[-1]

for i in range(n-1):
  cur = arr[i]

  start = i + 1
  end = n - 1

  while start <= end:
    mid = (start + end) // 2
    temp = cur + arr[mid]

    if abs(temp) < min_val:
      min_val = abs(temp)
      ans_a = arr[i]
      ans_b = arr[mid]

    if temp < 0:
      start = mid + 1
    else:
      end = mid - 1

print(ans_a,ans_b)