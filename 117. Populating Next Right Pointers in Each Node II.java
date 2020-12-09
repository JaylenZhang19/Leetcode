/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null){
            return null;
        }
        List<Node> previous = new ArrayList<>();
        previous.add(root);
        while(!previous.isEmpty()){
            List<Node> current_row = new ArrayList<>();
            for(int index = 0; index < previous.size(); index++){
                Node current = previous.get(index);
                if(current.left != null){
                    current_row.add(current.left);
                }
                if(current.right != null){
                    current_row.add(current.right);
                }
            }
            for(int index = 0; index < current_row.size() - 1; index++){
                current_row.get(index).next = current_row.get(index+1);
            }
            previous = current_row;
        }
        return root;
    }
}