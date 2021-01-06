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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-111, head);
        dummy.next = helper(head);
        return dummy.next;
    }
    
    public ListNode helper(ListNode node){
        if(node == null){
            return node;
        }
        ListNode cur = node.next;
        if(cur != null && cur.val == node.val){
            while(cur != null && cur.val == node.val){
                cur = cur.next;
            }
            return helper(cur);
        }
        node.next = helper(node.next);
        return node;
        
    }
}


class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-1111, head);
        ListNode p1 = dummy;
        
        while(p1 != null){
            ListNode p2 = p1.next;
            if(p2 == null){
                return dummy.next;
            }
            ListNode p3 = p2.next;
            if(p3 != null && p3.val == p2.val){
                while(p3 != null && p3.val == p2.val){
                    p3 = p3.next;
                }
                p1.next = p3;
            }
            else{
                p1 = p2;
            }
        }
        return dummy.next;
    }
}