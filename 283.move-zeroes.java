import java.util.List;

/*
 * @lc app=leetcode id=283 lang=java
 *
 * [283] Move Zeroes
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        int insertPtr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[insertPtr++] = nums[i];
            }
        }
        for (int i = insertPtr; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
// @lc code=end
