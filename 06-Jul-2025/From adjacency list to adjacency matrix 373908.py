# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())  # number of vertices

# initialize n x n matrix with 0
adj_matrix = [[0]*n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    k = data[0]           # number of outgoing edges for vertex i+1
    neighbors = data[1:]  # the destination vertices (1-based)

    for v in neighbors:
        adj_matrix[i][v-1] = 1  # convert to 0-based indexing

# print adjacency matrix
for row in adj_matrix:
    print(' '.join(map(str, row)))
