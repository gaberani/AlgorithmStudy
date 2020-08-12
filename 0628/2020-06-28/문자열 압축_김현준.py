def solution(s):
    N = len(s)
    answer = N
    # 문자열 압축 단위 길이
    for length in range(N, 0, -1):
        # 압축 결과
        tmp = ''
        # 압축 단위 단어들
        tmp_word = s[:length]
        # 압축 단위 단어 개수
        tmp_num = 1
        # 압축 단위씩 검사
        for k in range(length, N, length):
            # 압축 단어가 중복되면
            if tmp_word==s[k:k+length]:
                tmp_num += 1
            else:
                # 중복 안될 때 
                if tmp_num==1:
                    tmp += tmp_word
                else:
                    tmp += str(tmp_num)+tmp_word
                    tmp_num = 1
                tmp_word = s[k:k+length]
        # 검사 마친 후 남은 tmp 처리
        if tmp_num == 1:
            tmp += tmp_word
        else:
            tmp += str(tmp_num) + tmp_word
        # 압축 최소 길이 갱신
        answer = min(answer, len(tmp))
    return answer

# s = "aabbaccc"  # reulst = 7

# s = "ababcdcdababcdcd"  # reulst = 9

s = "abcabcdede"  # reulst = 8

# s = "abcabcabcabcdededededede"  # reulst = 14

# s = "xababcdcdababcdcd"  # reulst = 17

print(solution(s))