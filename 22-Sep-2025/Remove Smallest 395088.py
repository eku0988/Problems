# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()
    possible = True
    for i in range(n - 1):
        if a[i+1] - a[i] > 1:
            possible = False
            break
    print("YES" if possible else "NO")
