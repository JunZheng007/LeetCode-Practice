/*
 * @lc app=leetcode id=541 lang=java
 *
 * [541] Reverse String II
 */

// @lc code=start
class Solution {
    public String reverseStr(String s, int k) {
        char[] string = s.toCharArray();
        for (int i = 0; i < string.length; i += 2 * k) {
            if (string.length - i < k) {
                reverse(string, i, string.length);
                break;
            }
            reverse(string, i, i + k);
        }
        return String.valueOf(string);
    }

    private void reverse(char[] s, int start, int end) {
        for (int i = start, j = end - 1; i < j; i++, j--) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }
}
// @lc code=end

