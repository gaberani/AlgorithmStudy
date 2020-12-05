class Solution(object):
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


test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
print(test.groupAnagrams([""]))
# [[""]]
print(test.groupAnagrams(["a"]))
# [["a"]]