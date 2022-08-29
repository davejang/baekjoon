N, r, c = map(int,input().split())

def z(N,r,c):
  if N == 1:
    if r == 0 and c == 0:
      return 0
    elif r == 0 and c == 1:
      return 1
    elif r == 1 and c == 0:
      return 2
    else:
      return 3
  else:
    if r>=2**(N-1) and c>=2**(N-1):
      return 0.75*(2**(2*N)) + z(N-1,r-2**(N-1),c-2**(N-1))
    elif r<2**(N-1) and c>=2**(N-1):
      return 0.25*(2**(2*N)) + z(N-1,r,c-2**(N-1))
    elif r>=2**(N-1) and c<2**(N-1):
      return 0.5*(2**(2*N)) + z(N-1,r-2**(N-1),c)
    else:
      return z(N-1,r,c)

print(int(z(N,r,c)))