# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k=map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()
if nums[k-1] != nums[k]:
  print(nums[k-1]+1)
else:
  print(-1)