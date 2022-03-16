/*
 * @lc app=leetcode id=147 lang=java
 *
 * [147] Insertion Sort List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode curr = head.next;
        ListNode tail = head;
        while (curr != null) {
            if (head.val > curr.val) {
                tail.next = curr.next;
                curr.next = head;
                head = curr;
                curr = tail.next;
                continue;
            }
            if (tail.val <= curr.val) {
                tail = curr;
                curr = tail.next;
                continue;
            }
            ListNode prev = head;
            while (prev != curr) {
                if (prev.next.val <= curr.val) {
                    prev = prev.next;
                } else {
                    tail.next = curr.next;
                    curr.next = prev.next;
                    prev.next = curr;
                    curr = tail.next;
                    break;
                }
            }
        }
        return head;
    }
}
// @lc code=end

