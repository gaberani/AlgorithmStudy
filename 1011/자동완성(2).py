class Trie():
    def __init__(self):
        self.next = dict()
        self.value = 0

def solution(words):
    answer = 0
    tree = Trie()
    for word in words:
        subtree = tree
        # string을 enumerate하면 (인덱스, 문자 하나)로 나옴
        for idx, val in enumerate(word):
            print(idx, val)
            subtree.value += 1
            # 문자가 서브트리의 딕셔너리에 없으면 만듬
            if val not in subtree.next:
                subtree.next[val] = Trie()
            print(subtree.next)
            subtree = subtree.next[val]
            if (idx == len(word) - 1):
                subtree.value += 1

    for word in words:
        subtree = tree
        cnt = 0
        for idx, val in enumerate(word):
            if (subtree.value == 1):
                answer += cnt
                break
            elif idx == len(word) - 1:
                answer += cnt + 1
                break
            else:
                subtree = subtree.next[val]
                cnt += 1

    return answer

print(solution(["go", "gone", "guild"]))                # 7
print(solution(["abc", "def", "ghi", "jklm"]))          # 4
print(solution(["word", "war", "warrior", "world"]))    # 15

# def solution(words):
#     words.sort()
#     n, answer = len(words), 0
#     arr = [0]*n
#     for i in range(n-1):
#         cnt1, cnt2 = find(words[i], words[i+1])
#         # 최대값으로 갱신
#         arr[i], arr[i+1] = max(arr[i], cnt1), max(arr[i+1], cnt2)
#     return sum(arr)
#
# def find(s1, s2): # 두 개의 글자를 비교하는 함수
#     pre, cur = 0, 0
#     while 1:
#         pre += 1
#         # s1의 길이와 같아질 경우
#         if cur == len(s1):
#             return pre-1, pre
#         # s2의 길이와 같아질 경우
#         elif cur == len(s2):
#             return pre, pre-1
#         # 글자가 달라짐.
#         elif s1[cur] != s2[cur]:
#             return pre, pre # 다른 문자를 가질 때
#         cur += 1