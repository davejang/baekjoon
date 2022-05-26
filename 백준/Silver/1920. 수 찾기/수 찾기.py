n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort()

def bi_search(array,target,start,end):
  if start > end:
    return 0
  mid = (start + end) // 2
  if array[mid] == target:
    return 1
  elif array[mid] > target:
    return bi_search(array,target,start,mid-1)
  else:
    return bi_search(array,target,mid+1,end)

for i in b:
  print(bi_search(a,i,0,n-1))