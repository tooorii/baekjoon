
N = int(input())

for _ in range(N):
    score = 0
    total_score = 0
    response = list(input())
    for i in response:
        if i == 'O':
            score +=1
            total_score += score
        else:
            score = 0
    print(total_score)