import java.util.*;

/*
 * @lc app=leetcode id=18 lang=java
 *
 * [18] 4Sum
 */

// @lc code=start
class Solution {
    int len = 0;

    public List<List<Integer>> fourSum(int[] nums, int target) {
        len = nums.length;
        Arrays.sort(nums);
        return kSum(nums, target, 4, 0);
    }

    private List<List<Integer>> kSum(int[] nums, int target, int k, int index) {
        List<List<Integer>> result = new ArrayList<>();
        if (index >= len) {
            return result;
        }
        if (k == 2) {
            int l = index;
            int r = len - 1;
            while (l < r) {
                if (nums[l] + nums[r] == target) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[l]);
                    list.add(nums[r]);
                    result.add(list);

                    while (l < r && nums[l] == nums[l + 1]) {
                        l++;
                    }
                    l++;
                    while (l < r && nums[r] == nums[r - 1]) {
                        r--;
                    }
                    r--;
                }

                else if (nums[l] + nums[r] < target) {
                    l++;
                } else if (nums[l] + nums[r] > target) {
                    r--;
                }
            }

        }

        else {
            for (int i = index; i < len; i++) {
                List<List<Integer>> temp = kSum(nums, target - nums[i], k - 1, i + 1);
                if (temp != null) {
                    for (List<Integer> t : temp) {
                        t.add(nums[i]);
                        Collections.sort(t);
                    }
                    result.addAll(temp);
                }
            }
        }
        
        // remove duplicates
        HashSet<List<Integer>> tmp = new HashSet<List<Integer>>(result);
        result.clear();
        result.addAll(tmp);

        return result;
    }
}
// @lc code=end
