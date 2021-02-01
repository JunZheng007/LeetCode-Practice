from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if len(strs) == 0:
            return answer
        temp = strs[0]
        for a in strs:
            if len(a) < len(temp):
                temp = a
        for i in range(len(temp)):
            for j in range(len(strs)):
                if (strs[j][i] != temp[i]):
                    return answer
            answer = answer + temp[i]
        return answer


print(Solution().longestCommonPrefix([]))