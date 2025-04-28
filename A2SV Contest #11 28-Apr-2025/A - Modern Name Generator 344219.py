# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

t = int(input())
for _ in range(t):
  words = input().split()
  output=words[0][0] + words[1][0] + words[2][0] 
  print(output.lower())