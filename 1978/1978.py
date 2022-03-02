numberofnumbers = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    for factor in range (2,i):
        if i%factor == 0:
            numbers.append('composite')
        else:
            numbers.append('prime')

print(numbers.count('prime'))