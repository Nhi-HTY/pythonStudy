import collections


class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

inputArray = []
for i in range(5):
    n = input()
    inputArray.append(n)

solution = Solution()
print(solution.groupAnagrams(inputArray))