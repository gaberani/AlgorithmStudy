def solution(start, trr, visit, bottom):
    answer = True
    return answer

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
# print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))

# def dfs(start, tree, visit, bottom):
#     if len(tree.get(start)) > 1:
#         for i in tree.get(start):
#             if visit[i] == 0:
#                 visit[i] = 1
#                 dfs(i, tree, visit, bottom)
#                 print(visit)
#                 visit[i] = 0
#     else:   # 트리의 끝 도착
#         flag = 0
#         for b in bottom:
#             # 아직 모두 돈게 아니면
#             if visit[b] == 0:
#                 visit[b] = 1
#                 dfs(start, tree, visit, bottom)
#                 visit[b] = 0
#                 flag = 1
#         if not flag:
#             # print(visit)
#             pass
# def solution(n, path, order):
#     answer = True
#     tree = dict()
#     for p in path:
#         if p[0] in tree:
#             tree.get(p[0]).append(p[1])
#         else:
#             tree[p[0]] = [p[1]]
#         if p[1] in tree:
#             tree.get(p[1]).append(p[0])
#         else:
#             tree[p[1]] = [p[0]]
#     print(tree)
#     visit = [0]*n
#     visit[0] = 1
#     bottom = []
#     for i in tree.keys():
#         if len(tree.get(i)) == 1:
#             bottom.append(i)
#     dfs(0, tree, visit, bottom)
#     return answer