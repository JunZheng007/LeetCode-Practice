#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        reveal =[]
        
        return reveal
        
# @lc code=end
test = [17,13,11,2,3,5,7]
answer = Solution().deckRevealedIncreasing(test)
print(answer)
