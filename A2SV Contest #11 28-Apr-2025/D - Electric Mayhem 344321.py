# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s=input()
stack = []
for char in s:
    popped = False
    if stack and stack[-1] == char:
      stack.pop()  
      popped = True
    
    if not popped :
      stack.append(char)

if stack:
  print("NO")
else:
  print("YES")