#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        if n == 1:
            return 0
        while n > 1:
            temp = self.prime_factor(n)
            if temp == 1:
                count += n
                break
            else:
                count += temp
                n = n // temp
        return count

    def prime_factor(self, n: int) -> int:
        max = n // 2
        for i in range(2, max):
            if n % i == 0:
                return i
        return 1
            
        
# @lc code=end
