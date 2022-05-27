string = []
while True:
  sentence = str(input())
  if sentence == '.':
    break
  string.append(sentence)

for sentence in string:
  stack = []
  isTrue = 1
  for i in range(len(sentence)):
    if sentence[i] == '(' or sentence[i] == '[':
      stack.append(sentence[i])
    if sentence[i] == ')':
      if len(stack) == 0:
        print('no')
        isTrue = 0
        break
      else:
        a = stack.pop()
        if a == '[':
          print('no')
          isTrue = 0
          break
    if sentence[i] == ']':
      if len(stack) == 0:
        print('no')
        isTrue = 0
        break
      else:
        a = stack.pop()
        if a == '(':
          print('no')
          isTrue = 0
          break

  if len(stack) == 0 and isTrue == 1:
    print('yes')
  elif len(stack) !=0 and isTrue == 1:
    print('no')