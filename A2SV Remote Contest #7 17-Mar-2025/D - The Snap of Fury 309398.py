# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

def solve():
    n = int(input())
    claws = list(map(int, input().split()))

    d = [0] * (n + 2)

    for i in range(1,n+1):
        left = i - claws[i - 1]
        if left < 1:
            left = 1
        d[left] += 1
        d[i] -= 1

    prefix = 0
    kills = 0

    for i in range(1, n + 1):
        prefix += d[i]
        if prefix > 0:
            kills += 1
    

    print(n - kills)


if __name__ == "__main__":
    solve()
