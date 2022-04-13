k = int(input())
stack = []
result = 0

for i in range(k):
  n = int(input())
  if(i>0 and n == 0):
    stack.pop()
  else:
    stack.append(n)

for i in range(len(stack)):
  result = result + stack[i]

print(result)