destination = int(input())
roomno = 1
ilist = [0]
i = 1

while destination > roomno:
    ilist.append(i)
    roomno += 6*i
    i+=1

print(max(ilist) +1)