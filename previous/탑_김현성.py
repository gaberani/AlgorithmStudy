def solution(heights):
    lenh = len(heights)
    answer = [0]*lenh
    for n in range(lenh-1, -1, -1):
        for h in range(n-1, -1, -1):
            if heights[n] < heights[h]:
                answer[n] = h+1
                break
    return answer