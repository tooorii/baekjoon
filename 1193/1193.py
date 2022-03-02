nth = int(input())
nthrange = 0

i = 0
while True:
    if nth <= nthrange:
        break
    i += 1
    nthrange += i
    ndsum = i+1

if ndsum %2 != 0:
    n = (ndsum - 1) - (nthrange - nth)
    d = 1 + (nthrange - nth)
else:
    n = 1 + (nthrange - nth)
    d = (ndsum - 1) - (nthrange - nth)

print("{}/{}".format(n, d))