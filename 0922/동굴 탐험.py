# 1. 파이썬에서 트리 구조를 이용
def solution_tree(start, trr, visit, bottom):
    answer = True
    return answer

# 2. deque를 이용해서 만들기
def solution_deque(start, trr, visit, bottom):
    answer = True
    # 1-1. 모든 방을 적어도 한 번은 방문해야 합니다.
    # 1-2. 특정 방은 방문하기 전에 반드시 먼저 방문할 방이 정해져 있습니다.
    # 2-1. 이는 A번 방은 방문하기 전에 반드시 B번 방을 먼저 방문해야 한다는 의미입니다.
    # 2-2. 어떤 방을 방문하기 위해 반드시 먼저 방문해야 하는 방은 없거나 또는 1개 입니다.
    # 2-3. 서로 다른 두 개 이상의 방에 대해 먼저 방문해야 하는 방이 같은 경우는 없습니다.
    # 2-4. 어떤 방이 먼저 방문해야 하는 방이면서 동시에 나중에 방문해야 되는 방인 경우는 없습니다.


    return answer

print(solution_deque(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
# print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))


# https://hose0728.tistory.com/77 <- 디큐로 풀어낸 동굴 탐험

# *** 코테 당시 풀이 ***
#
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