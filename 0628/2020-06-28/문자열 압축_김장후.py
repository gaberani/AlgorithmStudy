def solution(s):
    minV = len(s)
    # range from 1 to len(s) // 2
    for i in range(1, len(s)//2+1):
        # set pivot
        pivot = s[:i]
        now = i
        ans = ''
        cnt = 1
        while True:
            # index가 총 단어의 길이보다 커지면
            if now + i > len(s):
                # 중복 단어가 존재하면
                if cnt >= 2:
                    ans += str(cnt) + pivot + s[now:]
                else:
                    ans += pivot + s[now:]
                break
            else:
                # pivot 다음 단어
                tmp = s[now:now + i]
                # pivot과 다음 단어가 다르면
                if pivot != tmp:
                    if cnt >= 2:
                        ans += str(cnt) + pivot
                    else:
                        ans += pivot
                    pivot = tmp
                    cnt = 1
                else:
                    cnt += 1
                # 만약 총 합이 최소값보다 작은 경우
                if len(ans) >= minV:
                    break
                # 현재 index를 기준 단어 수만큼 증가
                now += i
        if minV > len(ans):
            minV = len(ans)
    return minV


s = "aabbaccc"
print(solution(s))
s = "ababcdcdababcdcd"
print(solution(s))
s = "abcabcdede"
print(solution(s))
s = "abcabcabcabcdededededede"
print(solution(s))
s = "xababcdcdababcdcd"
print(solution(s))