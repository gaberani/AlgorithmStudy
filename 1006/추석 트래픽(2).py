# lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열로 되어 있으며,
# 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T
# 응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함
# 처리시간(T)는 0.001 ≦ T ≦ 3.000
def solution(lines):
    answer = 0
    # 각 요청마다의 처리시간 사이에 있는 로그 찾기
    return answer

print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"]))

# 7
print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]))

# def solution(lines):
#     answer = 0
#     N = len(lines)
#     # end_time change second
#     end_time = [int(line[11:13])*3600 + int(line[14:16])*60 + int(line[17:19]) + int(line[20:23])*(10 ** -3) for line in lines]
#     # start_time change second
#     start_time = [0] * N
#     for i in range(N):
#         tmp = float(lines[i][24:-1])
#         # start_time[i] = round(end_time[i] - tmp + 0.001, 3)
#         start_time[i] = end_time[i] - tmp + 0.001
#     # section pivot
#     total = start_time + end_time
#     maxV = 0
#     for start in total:
#         ans = 0
#         end = round(start + 1, 3)
#         for j in range(N):
#             if start <= start_time[j] < end:
#                 ans += 1
#             elif start <= end_time[j] < end:
#                 ans += 1
#             elif start_time[j] <= start and end_time[j] >= end:
#                 ans += 1
#         if ans > maxV:
#             maxV = ans
#     return maxV