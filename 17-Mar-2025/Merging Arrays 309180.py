# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A


n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

a=0
b=0
output=[]
while a<n and b<m:
  if arr1[a]<arr2[b]:
    output.append(arr1[a])
    a+=1
  elif arr1[a]>arr2[b]:
    output.append(arr2[b])
    b+=1
  else:
    output.append(arr1[a])
    output.append(arr2[b])
    a+=1
    b+=1

while b<m:
  output.append(arr2[b])
  b+=1
while a<n:
  output.append(arr1[a])
  a+=1

print(" ".join(map(str, output)))

    