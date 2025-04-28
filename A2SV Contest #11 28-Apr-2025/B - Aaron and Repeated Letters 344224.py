# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

s=input()
stack = []
for char in s:
    if stack and stack[-1] == char:
        stack.pop()  
    else:
        stack.append(char)
print(''.join(stack))