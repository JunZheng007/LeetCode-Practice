#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for one in range(size := len(nums)):
            if one > 0 and nums[one] == nums[one - 1]:
                continue

            left, right = one + 1, size - 1
            while left < right:
                if (sum := nums[one] + nums[left] + nums[right]) == 0:
                    if (temp := [nums[one], nums[left], nums[right]]) not in result:
                        result.append(temp)
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return result

# @lc code=end
