# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()
total=0
count=0
for i in range(n):
  total+=nums[i] 
  if total < t:
    count+=1

print(count)