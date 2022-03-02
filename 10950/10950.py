T = int(input())
# T = input()로만 해서 range에 처리가 잘 안 됨
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)