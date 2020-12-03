class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
print(test.groupAnagrams([""]))
# [[""]]
print(test.groupAnagrams(["a"]))
# [["a"]]