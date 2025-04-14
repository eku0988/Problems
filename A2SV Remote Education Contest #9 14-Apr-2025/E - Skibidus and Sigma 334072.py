# Problem: E - Skibidus and Sigma - https://codeforces.com/gym/603156/problem/E

for _ in range(int(input())):
    num_of_arrays, length_of_array = map(int, input().split())
    arrays = []
    
    for _ in range(num_of_arrays):
        a = list(map(int, input().split()))

        for i in range(1, length_of_array):
            a[i] += a[i-1]

        arrays.append(a)

    arrays.sort(key=lambda array: array[-1], reverse=True)

    result = 0
    end = 0

    for i in range(num_of_arrays):
        for j in range(length_of_array):
            result += end + arrays[i][j]
        end += arrays[i][-1]

    print(result)