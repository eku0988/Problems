# Problem: C - Mr. Boomsy - https://codeforces.com/gym/605795/problem/C

t = int(input())
for _ in range(t):
  s = input()
  stack=[]
  for char in s:
      if stack and char=='B':
          stack.pop()  
      else:
          stack.append(char)
  print(len(stack))