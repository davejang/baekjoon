import sys

input = sys.stdin.readline

s = str(input().rstrip())
s_explode = str(input().rstrip())
stack = []
length = len(s_explode)

for i in range(len(s)):
  stack.append(s[i])
  if ''.join(stack[-length:]) == s_explode:
    for j in range(length):
      stack.pop()

if not stack:
  print('FRULA')
else:
  print(''.join(stack))