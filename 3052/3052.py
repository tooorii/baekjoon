numbers = []
for _ in range(10):
    a = int(input())
    b = a%42
    numbers.append(b)
numbers = set(numbers)
print(len(numbers))