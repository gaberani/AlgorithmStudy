# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.
# 가장 멀리 떨어진 노드란
# 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드

# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향, 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다

# 노드의 개수 n
# 간선에 대한 정보가 담긴 2차원 배열 vertex
def solution(n, edges):
    # 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return
    answer = 0

    graph = [[0]*(n+1) for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1

    cnt_dic = {}

    def dfs(cnt, visit):

    # max_cnt = 1
    # for start in range(n+1):
    #     cnt = 0
    #     if graph[1][start]:
    #         col = start
    #         while graph[start][col]:
    #             for
    #             start = graph[start]
    #             cnt += 1
    #     if cnt > max_cnt:
    #         answer, max_cnt = 1, cnt
    #     elif cnt == max_cnt:
    #         answer += 1
    # return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))