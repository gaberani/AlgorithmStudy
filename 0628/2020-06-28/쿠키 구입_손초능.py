def solution(cookie):
    n = len(cookie)
    answer = 0

    for i in range(n-1):
        front = cookie[i]
        f_idx = i

        back = cookie[i+1]
        b_idx = i+1

        while f_idx >= 0 and b_idx < n:
            if front == back:
                answer = max(answer, front)
            if f_idx > 0 and front <= back:
                f_idx -= 1
                front += cookie[f_idx]
            elif b_idx < n-1 and front >= back:
                b_idx += 1
                back += cookie[b_idx]
            else: break

    return answer

print(solution([1, 1, 2, 3]))
print(solution([1, 2, 4, 5]))