H, M = map(int, input().split())
if M<45 and H==0:
    M+=15
    H=23
elif M<45 and H!=0:
    M+=15
    H-=1
else:
    M-=45
print(H,M)