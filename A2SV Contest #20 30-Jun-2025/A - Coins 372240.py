# Problem: A - Coins - https://codeforces.com/gym/618729/problem/A

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  max_y = n // k
  found = False
  # Try y = max_y down to a few lower values (at most 100 tries)
  for i in range(max(0, max_y - 100), max_y + 1):
      rem = n - i * k
      if rem >= 0 and rem % 2 == 0:
          found = True
          break
  print("YES" if found else "NO")
