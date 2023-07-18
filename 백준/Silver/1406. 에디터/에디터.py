import sys

input = sys.stdin.readline

stack1 = list(str(input().rstrip()))
stack2 = []
command = int(input())

for i in range(command):
    c = input().split()

    if c[0] == 'L':
      if stack1:
        stack2.append(stack1.pop())

    if c[0] == 'D':
      if stack2:
        stack1.append(stack2.pop())
          
    if c[0] == 'B':
      if stack1:
        stack1.pop()
          
    if c[0] == 'P':
      stack1.append(c[1])
      
print(''.join(stack1 + list(reversed(stack2))))