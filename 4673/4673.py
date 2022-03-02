numbers = list(range(10001))

def d(n):
    for n in range(1, 10000):
        d = n
        for i in len(str(n)):
            d += n[i]
    return d

for n in range(10001):
    numbers.remove(d(n))

print(*numbers, sep = '\n')