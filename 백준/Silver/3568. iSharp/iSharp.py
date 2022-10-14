s = str(input())
str_list = list(s.split(','))
word_list = []

for i in str_list:
  s = list(i.split(' '))
  for word in s:
    if word != '':
      word_list.append(word)

type_word = word_list[0]

for i in range(1,len(word_list)):
  string_out = type_word
  value_name = ''
  stack = []
  for j in range(len(word_list[i])):
    if word_list[i][j] != ';' and  word_list[i][j] != '[' and  word_list[i][j] != ']' and  word_list[i][j] != '*' and  word_list[i][j] != '&':
      value_name += word_list[i][j]
    else:
      if word_list[i][j] != ';':
        if word_list[i][j] == '[':
          stack.append(']')
        elif word_list[i][j] == ']':
          stack.append('[')
        else:
          stack.append(word_list[i][j])
  while stack:
    string_out += stack.pop()

  string_out += ' ' + value_name + ';'
  print(string_out)