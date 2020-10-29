# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
# 가장 멀리 떨어진 노드란
# 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드

# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향, 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다

# 노드의 개수 n
# 간선에 대한 정보가 담긴 2차원 배열 vertex
def solution(n, edges):
    def bfs():
        q = []
        q.append(1)

        while q:
            i = q.pop(0)
            for j in graph[i]:
                if visit[j] == -1:
                    visit[j] = visit[i]+1
                    q.append(j)

    graph = [[] for _ in range(n+1)]
    for i, j in edges:
        graph[i].append(i)
        graph[j].append(j)

    visit = [-1]*(n+1)
    visit[1] = 0

    bfs()
    print(visit)
    return visit.count(max(visit))

# def solution(n, edges):
#     # 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return
#     answer = 0
#
#     graph = [[0]*(n+1) for _ in range(n+1)]
#     for edge in edges:
#         graph[edge[0]][edge[1]] = 1
#         graph[edge[1]][edge[0]] = 1
#     for g in graph: print(g)
#     print(graph)
#
#     cnt_dic = {num: [] for num in range(n+1)}
#     for j in range(1, n+1):
#         # 1번 노드에 연결되는 곳이 있으면 시작
#         if graph[1][j]:
#             cnt_dic[0].append('1'+str(j))
#     print(cnt_dic)
#
#     cnt = 0
#     while 1:
#         for start in cnt_dic[cnt]:
#             for j in range(1, n+1):
#                 # print(int(start[-1]))
#                 if graph[int(start[-1])][j] and str(j) not in start:
#                     cnt_dic[cnt+1].append(start+str(j))
#         print(cnt_dic)
#         if cnt_dic[cnt+1] == []: break
#         cnt += 1
#     return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))