def d(n):
    a = str(n)
    c = 0
    for b in range(len(a)):
        c += int(a[b])
    d = c+n
    return d

integer_list = list(range(1, 10001))

e = 1
while d(e) < 10001:
    try:
        integer_list.remove(d(e))
        e+=1
    except:
        e+=1
        pass

print(*integer_list, sep = '\n')