testcase = int(input())

for _ in range(testcase):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    over = 0
    for i in range(arr[0]):
        if arr[i+1] > avg:
            over += 1
    print("{:.3f}%".format(over / arr[0] * 100))