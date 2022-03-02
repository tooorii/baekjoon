floor, ceiling = map(int, input().split())

isPrime = [False, False] + [True for _ in range(ceiling)]

for i in range(2, ceiling+1):
    if isPrime[i]:
        for j in range(i*i, ceiling+1, i):
            isPrime[j] = False

primes = []
for i in range(floor, ceiling+1):
    if isPrime[i]:
        primes.append(i)

for i in primes:
    print(i)