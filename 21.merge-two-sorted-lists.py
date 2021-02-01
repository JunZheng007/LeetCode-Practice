#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        res = ListNode()
        temp = res
        while p1 != None or p2 != None:
            temp.next = ListNode()
            temp = temp.next
            if p1 != None and p2 == None:
                temp.val = p1.val
                p1 = p1.next
            elif p1 == None and p2 != None:
                temp.val = p2.val
                p2 = p2.next
            elif p1.val <= p2.val:
                temp.val = p1.val
                p1 = p1.next
            else:
                temp.val = p2.val
                p2 = p2.next

        res = res.next

        return res

# @lc code=end

