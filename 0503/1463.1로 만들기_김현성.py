N = int(input())
memo = [0]*(N+1)
for i in range(2, N+1):
    memo[i] = memo[i-1] + 1
    if not i%2 and memo[i] > memo[i//2] + 1:
        memo[i] = memo[i//2] + 1
    if not i%3 and memo[i] > memo[i//3] + 1:
        memo[i] = memo[i//3] + 1
    # print(i, memo[i])
print(memo[N])

# def makeone(N, cnt, Tmemo, Bmemo):
#     global min_cnt
#     if N == 1:
#         if min_cnt > cnt:
#             min_cnt = cnt
#     else:
#         print(N, Tmemo, Bmemo)
#         if not N%3 and N//3 not in Tmemo:
#             Tmemo.append(N//3)
#             makeone(N//3, cnt+1, Tmemo, Bmemo)
#         elif not N%3 and cnt+1 < min_cnt:
#             makeone(N//3, cnt + 1, Tmemo, Bmemo)
#         if not N%2 and N//2 not in Bmemo:
#             Bmemo.append(N//2)
#             makeone(N//2, cnt+1, Tmemo, Bmemo)
#         elif not N%2 and cnt+1 < min_cnt:
#             makeone(N//2, cnt + 1, Tmemo, Bmemo)
#         makeone(N-1, cnt+1, Tmemo, Bmemo)
# N = int(input())
# min_cnt = 2*31-1
# makeone(N, 0, [], [])
# print(min_cnt)