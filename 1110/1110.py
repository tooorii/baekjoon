x = int(input())
N = 1

while 0<=x<99 :
    N+=1
    A, B = (x//10, x%10)
    y = A + B
    x = B + y%10
    
    if B == 0:
        break
print (N)