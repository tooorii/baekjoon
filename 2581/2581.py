def isPrime(num):
    if num ==1:
        return False
    for i in range(2, num):
        if i*i > num:
            break
        if num % i == 0:
            return False
    return True

lower = int(input())
upper = int(input())
primes = []
for num in range(lower, upper+1):
    if isPrime(num):
        primes.append(num)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)