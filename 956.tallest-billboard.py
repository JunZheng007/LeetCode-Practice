#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
import collections
# @lc code=start
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = dict()
        dp[0] = 0
        
        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s+i] = max(dp[s] + i, cur[s+i])
                cur[s] = max(dp[s], cur[s])
                cur[s-i] = max(dp[s], cur[s-i])
            dp = cur
        return dp[0]

        
# @lc code=end