N = int(input())

array = [['*' for col in range(N)] for row in range(N)]

def star(n,array,a,b):
  if n == 1:
    return True
  else:
    for i in range(int(a+int(n/3)),int(a+2*int(n/3))):
      for j in range(int(b+int(n/3)),int(b+int(2*n/3))):
        array[i][j] = ' '
    star(int(n/3),array,a,b)
    star(int(n/3),array,a+int(n/3),b)
    star(int(n/3),array,a+2*int(n/3),b)
    star(int(n/3),array,a,b+int(n/3))
    star(int(n/3),array,a,b+2*int(n/3))
    star(int(n/3),array,a+int(n/3),b+2*int(n/3))
    star(int(n/3),array,a+2*int(n/3),b+int(n/3))
    star(int(n/3),array,a+2*int(n/3),b+2*int(n/3))

star(N,array,0,0)

for i in range(N):
  print(''.join(array[i]))