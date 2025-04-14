# Problem: C - z-sort - https://codeforces.com/gym/603156/problem/C

t=int(input())
arr= list(map(int,input().split()))
for i in range(1, len(arr)):
    if i % 2 == 1:
      if arr[i] < arr[i - 1]:
          arr[i], arr[i - 1] = arr[i - 1], arr[i]
    else:
      if arr[i] > arr[i - 1]:
          arr[i], arr[i - 1] = arr[i - 1], arr[i]

print(*arr)
  

  