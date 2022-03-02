def isPrime(num):           #소수 찾기 함수
    if num ==1:
        return False
    for i in range(2, num): #2의 경우 범위가 안맞아서 아예 돌지 않아 True됨
        if num % i ==0:
            return False
    return True             #if들에 안 걸리면 소수로 True

_ = int(input())
cnt_answer = 0              #len보다 count가 빠름(정수연산)
for number in list(map(int, input().split())):
    if isPrime(number):
        cnt_answer +=1
print(cnt_answer)