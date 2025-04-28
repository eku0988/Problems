# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s=input()
n = len(s)
min_char_from = [''] * (n + 1)
min_char_from[n] = '{'  # character after 'z' in ASCII

# Precompute the minimum character from the end
for i in range(n - 1, -1, -1):
    min_char_from[i] = min(s[i], min_char_from[i + 1])

t = []
u = []
i = 0
while i < n or t:
    if not t:
        t.append(s[i])
        i += 1
    elif i < n and t[-1] > min_char_from[i]:
        t.append(s[i])
        i += 1
    else:
        u.append(t.pop())

print(''.join(u))