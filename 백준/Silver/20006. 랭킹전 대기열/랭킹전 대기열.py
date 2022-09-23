p, m = map(int,input().split())
room = []
for i in range(p):
  no_match = True
  n, l = map(str,input().split())
  n = int(n)   
  for i in room:
    if n >= i[0][0] - 10 and n <= i[0][0] + 10 and len(i) < m:
      i.append((n,l))
      no_match = False
      break
  if no_match == True:
    new_room = []
    new_room.append((n,l))
    room.append(new_room) 
for i in room:
  i.sort(key=lambda x:x[1])
  if len(i) == m:
    print('Started!')
    for j in i:
      print(j[0],j[1])
  else:
    print('Waiting!')
    for j in i:
      print(j[0],j[1])