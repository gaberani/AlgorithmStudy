def solution(cookie):
    answer = 0
    N = len(cookie)
    for i in range(N-1):
        left = i
        left_tmp = cookie[left]
        right = i+1
        right_tmp = cookie[right]
        while True:
            if left_tmp == right_tmp:
                if answer < left_tmp:
                    answer = left_tmp
            if left_tmp >= right_tmp and right < N-1:
                right += 1
                right_tmp += cookie[right]
            elif left_tmp < right_tmp and left > 0:
                left -= 1
                left_tmp += cookie[left]
            else:
                break
    return answer



cookie = [1,1,2,3]
print(solution(cookie))
cookie = [1,2,4,5]
print(solution(cookie))