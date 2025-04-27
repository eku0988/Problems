# Problem: A - How i met your mother - Last Forever - https://codeforces.com/gym/604857/problem/A

n = int(input())
s = input()

ones = s.count('n')  
zeros = s.count('z')  

result = ['1'] * ones + ['0'] * zeros
print(' '.join(result))
