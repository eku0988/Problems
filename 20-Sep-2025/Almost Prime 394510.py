# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def count_almost_primes(n):
    # Sieve for smallest prime factor (spf)
    spf = [0] * (n + 1)
    for i in range(2, n + 1):
        if spf[i] == 0:  # i is prime
            for j in range(i, n + 1, i):
                if spf[j] == 0:
                    spf[j] = i

    count = 0
    for x in range(2, n + 1):
        distinct_primes = set()
        num = x
        while num > 1:
            distinct_primes.add(spf[num])
            num //= spf[num]
        if len(distinct_primes) == 2:
            count += 1
    return count


n = int(input())
print(count_almost_primes(n))
