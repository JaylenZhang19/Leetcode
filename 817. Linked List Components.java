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
    public int numComponents(ListNode head, int[] G) {
        HashSet<Integer> seen = new HashSet<>();
        for(int val : G){
            seen.add(val);
        }
        boolean isComponent = false;
        int ret = 0;
        ListNode cur = head;
        while(cur != null){
            if(seen.contains(cur.val)){
                if(!isComponent){
                    ret += 1;
                }
                isComponent = true;
            }else{
                isComponent = false;
            }
            cur = cur.next;
        }
        return ret;
        
    }
}