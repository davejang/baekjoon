import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split()))
arr.sort()

start = 0
end = n - 1
min_value = int(1e10)
r1, r2, r3 = 0, 0, 0

for i in range(n-2):
  left = i+1
  right = n-1

  while left < right:
    cur_total = arr[i] + arr[left] + arr[right]

    if abs(cur_total) <= min_value:
      r1 = arr[i]
      r2 = arr[left]
      r3 = arr[right]
      min_value = abs(cur_total)

    if cur_total > 0:
      right -= 1
    elif cur_total < 0:
      left += 1
    else:
      break

print(r1,r2,r3)