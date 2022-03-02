T = int(input())
wordtypes = 0

for _ in range(T):
    word = input()
    isExist = set()

    isValid = True
    for i in range(len(word)):
        if word[i] not in isExist:
            isExist.add(word[i])
        elif word[i-1] != word[i]:
            isValid = False
    if isValid:
        wordtypes +=1
print(wordtypes)