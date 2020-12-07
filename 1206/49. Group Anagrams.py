class Solution(object):
    # 3320
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dic = []
        for str in strs:
            s_dic = {}
            # 한글자씩 따기
            for s in str:
                s_dic[s] = 1 if s_dic.get(s) == None else s_dic[s] + 1

            if str_dic:
                # print(s_dic, [k[0] for k in str_dic])
                if s_dic not in [k[0] for k in str_dic]:
                    str_dic.append([s_dic, str])
                else:
                    str_dic[[k[0] for k in str_dic].index(s_dic)].append(str)
            else:
                str_dic.append([s_dic, str])
        return [a[1:] for a in str_dic]

    # 100
    def Solution1(self, strs):
        d = {}
        for w in sorted(strs):
            # 왜 튜플인가? 요소값을 지우거나 변경할 수 없다. => 딕셔너리 키로 사용 가능
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
print(test.groupAnagrams([""]))
# [[""]]
print(test.groupAnagrams(["a"]))
# [["a"]]