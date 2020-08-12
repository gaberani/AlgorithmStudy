def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    alpa_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                 'o','p','q','r','s','t','u','v','w','x','y','z']
    ls1, ls2 = len(str1), len(str2)
    bs1, bs2 = [], []
    # str1 집합 만들기
    for i in range(ls1-1):
        if str1[i] in alpa_list and str1[i+1] in alpa_list:
            bs1.append(str1[i:i+2].lower())
    # str2 집합 만들기
    for j in range(ls2-1):
        if str2[j] in alpa_list and str2[j+1] in alpa_list:
            bs2.append(str2[j:j+2].lower())
    # str1과 str2 비교하면서 합집합, 교집합 만들기
    if len(bs1) <= len(bs2):
        hap, gyo, l1, l2 = bs2, [], list(set(bs1)), list(set(bs2))
    else:
        hap, gyo, l1, l2 = bs1, [], list(set(bs1)), list(set(bs2))
    for piece in l1:        # 더 긴쪽 리스트 기준
        if piece in l2:     # 짧은 쪽에 있나 체크
            for _ in range(min(bs1.count(piece), bs2.count(piece))):
                gyo.append(piece)   # 있으면 교집합
            if piece not in hap:    # 합집합에 없으면 붙여주자
                for _ in range(max(bs1.count(piece), bs2.count(piece))-1):
                    hap.append(piece)
        else:               # 짧은 쪽에 없네?
            if piece not in hap:    # 합집합에 없으면 붙여주자
                hap.append(piece)
    # 자카드 유사도에 65536 곱하고 정수부만 취하기
    if len(hap) != 0:
        answer = 65536*len(gyo)/len(hap)
    else:
        answer = 65536
    print(bs1, bs2, l1, l2)
    print(gyo, hap)
    return int(answer)

print(solution('FRANCE', 'french'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))