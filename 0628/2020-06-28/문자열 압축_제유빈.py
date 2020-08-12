def solution(s):
    ans = s
    # 자르는 단위 길이
    for n in range(1, len(s)):
        i = 0       # 알파벳 인덱스
        tmp = ''    # 압축 결과물 저장
        cur, cnt = '', 1   # 단위문자 저장, 단위문자 카운트
        while i < len(s):
            # 다음 단위문자와 같으면
            if s[i:i+n] == s[i+n:i+2*n]:
                cnt += 1
                cur = s[i:i+n]
            # 위 조건 해당 안되고 첫 번째 인덱스이면
            elif not i:
                tmp += s[i:i+n]
            # 이전에 저장된 값이 있으면 ex. ababab => 3ab
            elif cur:
                tmp += str(cnt) + cur
                cur, cnt = '', 1
            # 모두 해당 안되고 이전에 저장된 값도 없으면
            else:
                tmp += s[i:i+n]
            i += n
        # 저장된 압축 결과물이 있고, 초기 스트링이 아니고, 길이가 더 짧으면 저장
        if tmp and tmp != s and len(tmp) < len(ans):
            ans = tmp

    return len(ans)


print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd")) # 17    # check  14
print(solution("a"))    # 1
print(solution("abrabcabcadqabcabc")) # 14    # 18  abr2abcadq2abc
print(solution("aaaaaaaaaabbb"))   # 5
print(solution("abababaaaaaaaa"))    # 6
print(solution('abcdefghijklmnopqrstuvwxyz'*100))  # 29
print(solution("a"*1000))   # 5
print(solution("a"*100))    # 4
print(solution("a"*10))     # 3
print(solution("aaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaa")) # 8
print(solution("aabbcc"))   # 6
print(solution("aabbccaabbccdd"))  # 9