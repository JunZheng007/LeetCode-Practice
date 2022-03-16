#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        temp = self.countAndSay(n - 1)
        count = 1
        num = temp[0]
        say = ''
        for s in temp[1:]:
            if s == num:
                count += 1
            else:
                say += str(count)
                say += str(num)
                count = 1
                num = s
        say += str(count)
        say += str(num)
        return say
        
# @lc code=end

