def reverse_arr(arr, ans_len):
    arr = arr[::-1]
    for i in range(ans_len):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr

def solution(n):
    answer = [0]
    ans_len = 1
    if n > 1:
        for _ in range(1, n):
            answer = answer + [0] + reverse_arr(answer, ans_len)
            ans_len = ans_len*2+1
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))


# def solution(n):
#     answer = [0]
#     tmp = [0]
#     ans_len = 1
#     cnt = 1
#     if n > 1:
#         while cnt < n:
#             for i in range(ans_len):
#                 if not i % 2:
#                     tmp.insert(i*2+1-1, 0)
#                     tmp.insert(i*2+1+1, 1)
#             answer = tmp[:]
#             ans_len = ans_len*2+1
#             cnt += 1
#     return answer
