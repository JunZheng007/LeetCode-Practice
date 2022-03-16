/*
 * @lc app=leetcode id=143 lang=java
 *
 * [143] Reorder List
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
    public void reorderList(ListNode head) {
        if (head == null|| head.next == null) return;

        // find the middle node
        ListNode temp = head;
        ListNode middle = head;
        while (temp.next != null && temp.next.next != null) {
            middle = middle.next;
            temp = temp.next.next;
        }
        temp = middle.next;
        middle.next = null;
        middle = temp;
        
        // reverse the half after the middle node
        ListNode curr = middle.next;
        middle.next = null;
        while (curr != null) {
            temp = curr.next;
            curr.next = middle;
            middle = curr;
            curr = temp;
        }

        // reorder the list one by one
        ListNode p1 = head;
        ListNode p2 = middle;
        while (p2 != null) {
            temp = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p1 = p2.next;
            p2 = temp;
        }
    }
}
// @lc code=end

