#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        sample = {'(': 1, ')': 1, '{': 2, '}': 2, '[': 3, ']': 3}
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if len(stack) == 0 or sample[stack.pop()] != sample[i]:
                    return False
        return stack == []

# @lc code=end
