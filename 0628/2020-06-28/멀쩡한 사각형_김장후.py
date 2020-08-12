def solution(w,h):
    total = w*h
    sumV = w+h
    cnt, gcd = 2, 1
    while cnt <= w and cnt <= h:
        if not w % cnt and not h % cnt:
            gcd *= cnt
            w //= cnt
            h //= cnt
            cnt = 2
        else:
            cnt += 1
    answer = total-sumV+gcd
    return answer

print(solution(8, 12))