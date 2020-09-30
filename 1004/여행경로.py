# 항상 ICN 공항에서 출발

# 항공권 정보가 담긴 2차원 배열 tickets
def solution(tickets):
    global answer
    # 방문하는 공항 경로를 배열에 담아 return
    # 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
    # 주어진 항공권은 모두 사용해야 합니다.
    answer = []

    # 뒤쪽 알파벳 순서에 따라 재정렬
    # tickets = sorted(tickets, key=lambda x: x[1])
    def dfs(tmp_lst, visit):
        if len(tmp_lst) == len(tickets)+1:
            # deepcopy 과정
            possible_answer = []
            for tmp in tmp_lst:
                possible_answer.append(tmp)
            answer.append(possible_answer)
        else:
            for i in range(len(tickets)):
                # 도착지와 출발지가 같으면 & 방문 안한 곳이면
                if tmp_lst[-1] == tickets[i][0] and visit[i] == 0:
                    visit[i] = 1
                    tmp_lst.append(tickets[i][1])
                    dfs(tmp_lst, visit)
                    tmp_lst.pop()
                    visit[i] = 0

    dfs(["ICN"], [0]*len(tickets))
    answer = sorted(answer)[0]
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],
                ["ATL", "ICN"], ["ATL","SFO"]]))