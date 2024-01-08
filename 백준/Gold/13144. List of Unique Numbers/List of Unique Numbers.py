import sys

input = sys.stdin.readline

n = int(input())
dp = [False] * 100001
arr = list(map(int,input().rstrip().split()))

left = 0
right = 0
result = 0

while left < n and right < n:
  if not dp[arr[right]]:
    dp[arr[right]] = True
    right += 1
    result += (right - left)
  else:
    dp[arr[left]] = False
    left += 1

print(result)