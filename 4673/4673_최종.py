def d_func(num):
    return num + sum(num // 10**i %10 for i in range(5)) #sum 안에서 for문 사용

isSelfNum = [False] + [True for _ in range(10000)]
for i in range(1, 10001):
    if isSelfNum[i]:
        print(i)
    if d_func(i) <= 10000:
        isSelfNum[d_func(i)] = False