lower = int(input())
upper = int(input())

isPrime = [False, False] + [True for _ in range(upper)]
#인덱스가 소수면 true 아니면 false 저장돼있게 할 것. 여기서부터 false로 바꿔줄 것.
# 일단 0, 1은 소수 아니고 2부터임
for i in range(2, upper +1):
    if isPrime[i]:
        for j in range(i*i, upper+1, i):
            #i가 11이라고 하면. 11*2부터 원래 지웠는데 11*2는 2를 지울 때 이미 지워졌을 거 아냐?
            #2 3 마찬가지고 11*4도 2 돌릴 때 지워졌겠지?
            #그래서 11보다 낮은 숫자에 대해서는 다 지워진 상태. 따라서 제곱수부터 시작해서 지워나가기 시작하면 된다
            isPrime[j] = False

primes = []
for i in range(lower, upper+1):
    if isPrime[i]:
        primes.append(i)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)