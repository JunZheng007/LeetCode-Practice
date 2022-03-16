/*
 * @lc app=leetcode id=189 lang=java
 *
 * [189] Rotate Array
 */

// @lc code=start
class Solution {
    public void rotate(int[] nums, int k) {
        // if k % nums.length == 0, then not need to rotate
        k %= nums.length;
        if (k == 0) {
            return;
        }
        // Solution 1
        // for (int i = 0; i < k; i++) {
        //     int temp = nums[nums.length - 1];
        //     for (int j = nums.length - 1; j > 0; j--) {
        //         nums[j] = nums[j - 1];
        //     }
        //     nums[0] = temp;
        // }

        // Solution 2
        // int[] result = new int[nums.length];
        // for (int i = 0; i < result.length; i++) {
        //     result[i] = nums[(nums.length + i - k) % nums.length];
        // }
        // for (int i = 0; i < result.length; i++) {
        //     nums[i] = result[i];
        // }

        // Solution 3
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}

// @lc code=end

