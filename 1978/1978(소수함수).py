numberofnumbers = int(input())
numbers = list(map(int, input().split()))
numbertype = []

def test(num):
    while num > 2:
        for i in range(2, num):
            if num %i == 0:
                break
            else:
                numbertype.append('prime')

for n in numbers:
    test(n)

print(len(numbertype))