





















# 기존 정답 코드
# class Node(object):
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}
#
#
# class Trie(object):
#     def __init__(self):
#         self.head = Node(None)
#
#     def insert(self, string):
#         curr_node = self.head
#         for char in string:
#             if char not in curr_node.children:
#                 curr_node.children[char] = Node(char)
#             curr_node = curr_node.children[char]
#         curr_node.data = string
#
#     def search(self, prefix):
#         curr_node = self.head
#         search_cnt = prefix.count('?') - 1
#         result_cnt = 0
#         dep_cnt = 0
#         subtrie = None
#
#         for char in prefix:
#             if char in curr_node.children:
#                 curr_node = curr_node.children[char]
#                 subtrie = curr_node
#             elif char is '?':
#                 break
#             else:
#                 return result_cnt
#
#         queue = list(subtrie.children.values())
#         queue_len = len(queue)
#
#         if search_cnt > 0:
#             while queue:
#                 if queue_len < 1:
#                     dep_cnt = dep_cnt + 1
#                     if dep_cnt == search_cnt:
#                         break
#                     else:
#                         queue_len = len(queue)
#                 curr = queue[0]
#                 queue.remove(curr)
#                 queue += list(curr.children.values())
#                 queue_len = queue_len - 1
#             # curr = queue.pop()
#             # if curr.data != None:
#             #     result.append(curr.data)
#         for q in queue:
#             if q.data != None:
#                 result_cnt = result_cnt + 1
#         return result_cnt
#
#
# def solution(words, queries):
#     answer = []
#     searched_lst = {}  # 중복 검색 제거용 리스트
#
#     prefix_trie = Trie()  # 접두사 검색 트리 만들기
#     for word in words:
#         prefix_trie.insert(word)
#
#     suffix_trie = Trie()  # 접미사 검색 트리 만들기
#     for word in words:
#         reverse_word = word[::-1]
#         suffix_trie.insert(reverse_word)
#
#     for query in queries:
#         cnt = 0
#         queue_len = len(query)
#
#         # 이미 검색된건지 체크
#         if query in searched_lst.keys():
#             answer.append(searched_lst.get(query))
#             continue
#
#         # 끝이 '?' 라면
#         if query[queue_len - 1] == '?':
#             # 처음도 '?' 라면
#             if query[0] == '?':
#                 for word in words:  # 길이 비교
#                     if len(word) == queue_len:
#                         cnt = cnt + 1
#                 answer.append(cnt)
#             else:  # 처음 '?' X -> 접두사 검색
#                 cnt = prefix_trie.search(query)
#                 answer.append(cnt)
#         else:  # 끝이 '?' X -> 접미사 검색
#             reverse_q = query[::-1]
#             cnt = suffix_trie.search(reverse_q)
#             answer.append(cnt)
#
#         # 중복 체크용 딕셔너리에 추가
#         searched_lst[query] = cnt
#     return answer
#
#
# print(solution(["frodo", "front", "frost", "frozen", "frame", "KaKao"],
#                ["fro??", "????o", "fr???", "fro???", "pro?"]))