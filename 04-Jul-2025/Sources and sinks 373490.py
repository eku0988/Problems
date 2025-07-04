# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986


n = int(input())

adj = [list(map(int, input().split())) for _ in range(n)]

sources = []
sinks = []

for i in range(n):
    if all(adj[i][j] == 0 for j in range(n)):
        sinks.append(i + 1)  # 1-based indexing

        if all(adj[j][i] == 0 for j in range(n)):
        sources.append(i + 1)

print(len(sources), *sorted(sources))

print(len(sinks), *sorted(sinks))
