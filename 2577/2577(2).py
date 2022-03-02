A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))

arr = [0]*10
for i in result:
	arr[int(i)] += 1

for i in range(10):
	print(arr[i])