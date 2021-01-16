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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        int val = l1.val + l2.val;
        int add = val / 10;
        val = val % 10;
        ListNode root = new ListNode(val);
        root.next = helper(l1.next, l2.next, add);
        return root;
    }
    
    public ListNode helper(ListNode l1, ListNode l2, int add){
        ListNode root = null;
        if(add >= 1){
            root = new ListNode(add);
        }
        if(l1 == null && l2 == null){
            return root;
        }
        int val = add;
        if(l1 == null){
            val += l2.val;
            add = val / 10;
            val = val % 10;
            root = new ListNode(val);
            root.next = helper(null, l2.next, add);
        }
        else if(l2 == null){
            val += l1.val;
            add = val / 10;
            val = val % 10;
            root = new ListNode(val);
            root.next = helper(l1.next, null, add);
        }
        else{
            val += (l1.val + l2.val);
            add = val / 10;
            val = val % 10;
            root = new ListNode(val);
            root.next = helper(l1.next, l2.next, add);
        }
        
        return root;
    }
}