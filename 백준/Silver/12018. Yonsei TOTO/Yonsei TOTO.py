import sys

input = sys.stdin.readline

n, m = map(int,input().split())
arr = []
count = 0

for i in range(n):
  p, l = map(int,input().split())
  m_list = list(map(int,input().rstrip().split()))
  m_list.sort(reverse=True)

  if p >= l:
    cutline = m_list[l-1]
    arr.append(cutline)
  else:
    arr.append(1)

arr.sort()
for i in arr:
  if m - i >= 0:
    m -= i
    count += 1
  else:
    break
    
print(count)