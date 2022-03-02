while True:
    try:
        A, B = map(int, input().split())
        0<A and B<10
        print (A+B)
    except:
        break