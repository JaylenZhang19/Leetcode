class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        int n = s.length();
        for(int i = 0; i < n; i++){
            if(s.charAt(i) == 'c'){
                if(stack.size() >= 2){
                    char most_top = stack.pop();
                    char second_top = stack.pop();
                    if (most_top == 'b' && second_top == 'a'){
                        continue;
                    }
                    else{
                        return false;
                    }
                }else{
                    return false;
                }
            }
            else{
                stack.push(s.charAt(i));
            }
        }
        return stack.size() == 0 ? true : false;
    }
}