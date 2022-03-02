T = int(input())
wordtypes = []

for _ in range(T):
    word = input()
    isExist = {}
    for i in range(ord('a'), ord('z')+1):
        isExist[str(i)] = False

    for i in range(len(word)):
        if isExist[word[i]] == False and word[i] == word[i+1]:
            isExist[word[i]] = False
        elif isExist[word[i]] == False and word[i] != word[i+1]:
            isExist[word[i]] = True
        else:
            isExist[word[i]] = False
    if word.count(False) > 0:
        word = False
    else:
        word = True
    wordtypes.append(word)

print(wordtypes.count(False))