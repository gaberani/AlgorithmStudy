# 첫째 아들: l번 바구니 ~ m번 바구니, 둘째 아들 m+1번 바구니 ~ r번 바구니까지
# 1 <= l <= m / m+1 <= r <= N
# 두 아들이 받을 과자 수는 같아야 합니다
# 이분탐색?
def solution(cookie):
    answer = 0
    L = len(cookie)
    for i in range(L-1):
        S_val, S_idx = cookie[i], i
        E_val, E_idx = cookie[i+1], i+1
        while 1:
            # 최대값 갱신
            if S_val == E_val and S_val > answer:
                answer = S_val

            # 쿠키 인덱스 넘어가지 않고, val 값 누가 큰지 따라 다르게
            if S_idx > 0 and S_val <= E_val:
                S_idx -= 1
                S_val += cookie[S_idx]
            elif E_idx < L-1 and S_val >= E_val:
                E_idx += 1
                E_val += cookie[E_idx]
            else:
                break
    return answer

print(solution([1,1,2,3]))
print(solution([1,2,4,5]))