N = int(input())
primeFactors = []

if N !=1:
    for i in range(2, N+1):
        while N%i ==0:
            primeFactors.append(i)
            N = N/i

    for i in primeFactors:
        print(i)