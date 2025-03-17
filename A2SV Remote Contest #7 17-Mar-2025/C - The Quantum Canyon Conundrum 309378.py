# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

t=int(input())
for _ in range(t):
  n=int(input())
  arr1=list(map(int,input().split()))
  if n==1:
    print("YES")
    continue

  c=0
  d=0
  while d<n:
    start_flat=d
    while d<n and arr1[d]==arr1[start_flat]:
      d+=1
    end_f=d-1

    g=True
    if start_flat>0 and arr1[start_flat]>arr1[start_flat-1]:
        g=False
    if end_f<n-1 and arr1[end_f]>=arr1[end_f+1]:
        g=False
      
    if g:
      c+=1

    if c>1:
      print("NO")
      break
  if c==1:
    print("YES")