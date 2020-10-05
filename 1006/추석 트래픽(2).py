def solution(lines):
    answer = 0
    return answer

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