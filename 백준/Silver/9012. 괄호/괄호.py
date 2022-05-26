n = int(input())
string_list = []
for i in range(n):
  string_list.append(str(input()))

def checkVPS(string):
  stack = 0
  for i in range(len(string)):
    if string[i] == '(':
      stack = stack + 1
    elif string[i] == ')':
      stack = stack - 1
    if stack < 0:
      return 'NO'
  if stack == 0:
    return 'YES'
  else:
    return 'NO'

for i in string_list:
  print(checkVPS(i))