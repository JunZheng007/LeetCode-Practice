#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = None
        i = 0
        while i < len(nums):
            if nums[i] == temp:
                nums.remove(nums[i])
            else:
                temp = nums[i]
                i += 1
        return len(nums)
        
# @lc code=end
