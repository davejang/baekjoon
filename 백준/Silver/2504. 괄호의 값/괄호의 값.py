s = str(input())
stack = []
result = 0
temp = 1

for c in s:
  if c == '(':
    temp *= 2
    stack.append(c)
  elif c == '[':
    temp *= 3
    stack.append(c)
  elif c == ')':
    if not stack or stack[-1] == '[':
      result = 0
      break
    if last_chr == '(':
      result += temp
    stack.pop()
    temp //= 2
  elif c == ']':
    if not stack or stack[-1] == '(':
      result = 0
      break
    if last_chr == '[':
      result += temp
    stack.pop()
    temp //= 3
  
  last_chr = c

if stack:
  result = 0
      
print(result)