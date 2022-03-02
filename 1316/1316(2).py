T = int(input())
wordtypes = []


for _ in range(T):
    word = input()

    compact = []    # 리스트를 만들어서 word의 알파벳을 하나씩 추가하되 연속된 중복값들은 추가 안할꺼야
                    # carret을 넣었다면 c, a, r, e, t
                    # abcabc를 넣었다면 a, b, c, a, b, c

    for a in range(len(word)):
        if (a < len(word) - 1):
            if word[a] != word[a+1]:
                compact.append(word[a])
        elif (a == len(word) - 1):
            compact.append(word[a])

    if (len(compact) == len(set(compact))): # set은 중복된 아이들을 제외하고 요소를 보여주는 함수, 중복된 아이들이 있다면 list의 구성원 수가 다르겠지
                                            # 이미 연속된 중복 알파벳을 제거했으니 여기서 중복된 아이가 있다면 그건 그룹단어가 아니야
        wordtypes.append(True)
    else:
        wordtypes.append(False)

print(wordtypes.count(True))    # 마지막으로 내가 필요한 True의 갯수만큼만 print