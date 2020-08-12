# def solution(cookie):     # 효율성 실패
#     answer = 0
#     N = len(cookie)
#     for s in range(N-1):
#         for e in range(s+2, N+1):
#             tmp = cookie[s:e]
#             second = sum(tmp)
#             if second > answer:
#                 first = 0
#                 i = 0
#                 while first <= second:
#                     first += tmp[i]
#                     second -= tmp[i]
#                     i += 1
#                     if first==second:
#                         if answer < first:
#                             answer = first
#                         break
#     return answer

def solution(cookie):
    answer = 0
    N = len(cookie)
    # i번 바구니~m번 바구니, m+1번 바구니~r번 바구니 [m: 경계 인덱스]
    for m in range(N-1):
        # 첫째 아들
        first_idx, first = m, cookie[m]
        # 둘째 아들
        second_idx, second = m+1, cookie[m+1]
        # 경계 인덱스를 중심으로 양쪽으로 넓혀 나간다
        # 둘 중 과자 수가 적은 쪽으로 점차 넓혀 간다
        while 1:
            if first==second:
                if answer < first:
                    answer = first
            if first >= second:
                second_idx += 1
                if second_idx<N:
                    second += cookie[second_idx]
                else:
                    break
            else:
                first_idx -= 1
                if first_idx>=0:
                    first += cookie[first_idx]
                else:
                    break
    return answer

cookie = [1,1,2,3]
# result = 3

# cookie = [1,2,4,5]
# # result = 0

print(solution(cookie))