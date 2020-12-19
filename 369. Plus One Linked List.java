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
    public ListNode plusOne(ListNode head) {
        int add = helper(head);
        if(add == 1){
            ListNode new_head = new ListNode(1, head);
            return new_head;
        }else{
            return head;
        }
    }
    
    public int helper(ListNode node){
        if(node == null){
            return 1;
        }
        int add = helper(node.next);
        node.val += add;
        int ret = node.val / 10;
        node.val = node.val % 10;
        return ret;
    }
}