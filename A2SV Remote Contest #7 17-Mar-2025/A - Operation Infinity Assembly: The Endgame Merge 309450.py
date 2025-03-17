# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

t = int(input())  # Number of test cases
for _ in range(t):
    n,m, k = map(int, input().split())  # Read m and k
    a = input().strip()
    b = input().strip()

    a = sorted(a)  # Sort string a
    b = sorted(b)  # Sort string b

    c = []  # Merged result
    results = []
    
    count_a, count_b = 0, 0  # Counters for consecutive elements from a and b
    i, j = 0, 0  # Pointers for a and b

    while i < len(a) and j < len(b):  # Merge until both lists are exhausted
        # Choose from a if it’s smaller and within the k-limit, or if b exceeds the limit
        if (a[i] < b[j] and count_a < k) or count_b >= k:
            c.append(a[i])
            i += 1
            count_a += 1
            count_b = 0  # Reset count_b when taking from a
        else:  # Otherwise, choose from b
            c.append(b[j])
            j += 1
            count_b += 1
            count_a = 0  # Reset count_a when taking from b

    results.append("".join(c))

    for result in results:
        print(result)
