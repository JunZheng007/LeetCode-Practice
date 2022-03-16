import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=525 lang=java
 *
 * [525] Contiguous Array
 */

// @lc code=start
class Solution {
    public int findMaxLength(int[] nums) {
        int maxLength = 0, count = 0;
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        m.put(0, 0);

        for (int i = 0; i < nums.length; i++) {
            count += nums[i] == 1 ? 1 : -1;
            if (m.getOrDefault(count, -1) != -1) {
                maxLength = Math.max(maxLength, i - m.get(count) + 1);
            } else {
                m.put(count, i + 1);
            }
        }

        return maxLength;
    }
}
// @lc code=end

