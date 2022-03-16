#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        x = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in text:
            if i in x.keys():
                x[i] += 1
        x['l'] /= 2
        x['o'] /= 2
        return int(min(x.values()))
        
# @lc code=end

