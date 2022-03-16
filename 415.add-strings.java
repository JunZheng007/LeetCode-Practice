/*
 * @lc app=leetcode id=415 lang=java
 *
 * [415] Add Strings
 */

// @lc code=start
class Solution {
    public String addStrings(String num1, String num2) {
        int len = Math.max(num1.length(), num2.length()) + 1;
        int i = num1.length(), j = num2.length(), k = len - 1;
        char[] sum = new char[len];
        int carry = 0;
        for (; i > 0 && j > 0; i--, j--, k--) {
            int n1 = num1.charAt(i - 1) - 48;
            int n2 = num2.charAt(j - 1) - 48;
            int temp = n1 + n2 + carry;
            sum[k] = (char) (temp % 10 + '0');
            carry = temp / 10;
        }
        while (i > 0) {
            int n1 = num1.charAt(i - 1) - 48;
            int temp = n1 + carry;
            sum[k] = (char) (temp % 10 + '0');
            carry = temp / 10;
            i--;
            k--;
        }
        while (j > 0) {
            int n2 = num2.charAt(j - 1) - 48;
            int temp = n2 + carry;
            sum[k] = (char) (temp % 10 + '0');
            carry = temp / 10;
            j--;
            k--;
        }
        if (carry > 0)
            sum[k] = (char) (carry + '0');

        if (sum[0] == '\0') {
            sum[0] = '0';
            String result = new String(sum);
            result = result.substring(1);
            return result;
        }
        else {
            String result = new String(sum);
            return result;
        }
    }
}
// @lc code=end

