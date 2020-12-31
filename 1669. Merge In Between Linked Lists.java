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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode l2_tail = list2;
        while(l2_tail.next != null){
            l2_tail = l2_tail.next;
        }
        int index = 0;
        ListNode current = list1;
        while(current != null){
            if(index == a - 1){
                ListNode previous = current;
                current = current.next;
                previous.next = list2;
            }
            else if(index == b){
                l2_tail.next = current.next;
                return list1;
            }
            else{
                current = current.next;
            }
            index ++;
        }
        return list1;
    }
}