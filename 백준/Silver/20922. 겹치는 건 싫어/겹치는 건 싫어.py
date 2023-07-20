import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

left = 0
right = 0
result = 1
dp = [0] * (max(arr) + 1)

while right < n:
  if dp[arr[right]] < k:
    dp[arr[right]] += 1
    right += 1
  else:
    dp[arr[left]] -= 1
    left += 1
  result = max(result,right-left)

print(result)