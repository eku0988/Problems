# Problem: C - The big bang theory -  The Stockholm Syndrome - https://codeforces.com/gym/604857/problem/C

n=int(input())
arr= list(map(int,input().split()))
arr.sort()
mex = 1
for x in arr:
    if x >= mex:
        mex += 1
print(mex)