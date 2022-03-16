/*
 * @lc app=leetcode id=459 lang=java
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String ss = s + s;
        for (int i = 1; i < s.length(); i++) {
            String temp = ss.substring(i, i + s.length());
            if (s.equals(temp)) 
                return true;
        }
        return false;
    }
}
// @lc code=end

