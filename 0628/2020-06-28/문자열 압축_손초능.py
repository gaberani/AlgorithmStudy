def solution(s):
    n, min_len = len(s), len(s)
    for i in range(1, n):
        string, cnt, total = s[0:i], 1, 0
        for j in range(1, n//i):
            if string == s[i*j:i*(j+1)]: cnt += 1
            else:
                if cnt != 1: total += len(str(cnt))
                total += i
                string = s[i * j:i * (j + 1)]
                cnt = 1
        if cnt != 1: total += len(str(cnt))
        total += i + n%i
        min_len = min(min_len, total)
    return min_len

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))