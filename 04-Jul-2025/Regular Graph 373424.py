# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict

# Read number of nodes and edges in one line
n, m = map(int, input().split())  # e.g., input: 3 3

# Initialize degree counter
degree = defaultdict(int)

# Read edges and update degrees
for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1

# Ensure all nodes are represented in the degree map
for i in range(1, n + 1):
    degree[i] += 0

# Get the degrees
degrees = list(degree.values())

# Check if all degrees are the same
is_regular = all(deg == degrees[0] for deg in degrees)
print("YES" if is_regular else "NO")
