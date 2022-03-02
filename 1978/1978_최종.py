def isPrime(num):
    if num ==1:
        return False
    for i in range(2, num):
        if i*i > num:
            break       #이때까지 안 나오면 앞으로도 안 나옴
        if num % i == 0:
            return False
    return True

_ = int(input())
cnt_answer = 0
for number in list(map(int, input().split())):
    if isPrime(number):
        cnt_answer += 1
print(cnt_answer)