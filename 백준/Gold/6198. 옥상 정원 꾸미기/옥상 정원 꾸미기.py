import sys

input = sys.stdin.readline

arr = []
stack = []

n = int(input())
result = 0

for i in range(n):
  arr.append(int(input()))

for i in range(n):
  while stack and arr[stack[-1]] <= arr[i]:
    stack.pop()
    result += len(stack)

  stack.append(i)


print(result + (len(stack) * (len(stack) - 1))//2)