# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.

def solution(s):
    L = len(s)
    if L == 1:
        return L
    answer = L
    for l in range(1, L//2+1):    # 자를 단위(절반까지 가능)
        cut_answer = ''
        word = s[:l]
        cnt = 1
        for sl in range(l, L, l):   # 단위만큼만 비교
            if word == s[sl:sl+l]:
                cnt += 1
            else:
                if cnt == 1:
                    cut_answer += word
                else:
                    cut_answer += str(cnt) + word
                    cnt = 1     # cnt 초기화
                word = s[sl:sl+l]

        # 끝난 뒤 마지막 부분에 따라 추가
        if cnt == 1:
            cut_answer += word
        else:
            cut_answer += str(cnt) + word

        if answer > len(cut_answer):
            answer = len(cut_answer)
    return answer

# print(solution('abcabcabc'))
# print(solution('aaabbbaaaaaaaaaaaa'))   # 3a3b12b
# print(solution('abrabcabcadqabcabc'))
# print(solution('aaaaaaaaaabbb'))
# print(solution('b'))
# print(solution('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
print(solution('aabbaccc'))                     # 7
print(solution("ababcdcdababcdcd"))             # 9
print(solution("abcabcdede"))                   # 8
print(solution("abcabcabcabcdededededede"))     # 14
print(solution("xababcdcdababcdcd"))            # 17