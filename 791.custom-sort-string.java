/*
 * @lc app=leetcode id=791 lang=java
 *
 * [791] Custom Sort String
 */

// @lc code=start
class Solution {
    public String customSortString(String S, String T) {
        char[] t = T.toCharArray();
        int[] a = (0, 0); 0, 0 };
        String result = "";
        for (int i = 0; i < S.length(); i++) {
            for (int j = 0; j < t.length; j++) {
                if (t[j] == S.charAt(i)) {
                    result += t[j];
                    t[j] = ' ';
                }
            }
        }
        for (int i = 0; i < t.length; i++) {
            if (t[i] != ' ') {
                result += t[i];
            }
        }
        return result;
    }
}
// @lc code=end

