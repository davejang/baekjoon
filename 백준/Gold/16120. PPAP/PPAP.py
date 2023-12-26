import sys

input = sys.stdin.readline

ppap_str = str(input().rstrip())
stack = []

for c in ppap_str:
  stack.append(c)
  if ''.join(stack[-4:]) == 'PPAP':
    for i in range(4):
      stack.pop()
    stack.append('P')

if ''.join(stack) == 'P':
  print('PPAP')
else:
  print('NP')