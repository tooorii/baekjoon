ceiling = int(input())

if ceiling <100:
    print(ceiling)

else:
    if ceiling == 1000:
        ceiling = 999

    hansu = []
    for i in range(100, ceiling+1):
        placeValue = []

        for j in range(3):
            placeValue.append(i//(10**j)%10)

        if placeValue[0] + placeValue[2] == placeValue[1]*2:
            hansu.append(i)
            
    print(len(hansu)+99)