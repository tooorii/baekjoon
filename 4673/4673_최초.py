def d_func(num):
    answer = num            #자기자신
    while num > 0:
        answer += num%10    #1의자리(ex: 12345의 '5')
        num //=10           #한자리 땡기기 (12345--> 1234)
    return answer           #결국 자기자신 + 각 자리 숫자 더한 값 나옴

isSelfNum = [False] + [True for _ in range(10000)] #0자리에 false 그 뒤에 1~10000까지 true로 설정
for i in range(1, 10001):
    if d_func(i) <= 10000:
        isSelfNum[d_func(i)] = False    #d(n)을 통해 나온 수는 셀프넘버 아님
for i in range(1, 10001):
    if isSelfNum[i]:                    #True인 애들만 print
        print(i)