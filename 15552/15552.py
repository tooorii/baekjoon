T = int(input())

for _ in range(T):
    import sys
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

    # readline 뒤에 () 안붙여서 오류남