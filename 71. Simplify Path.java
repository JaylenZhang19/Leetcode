class Solution {
    public String simplifyPath(String path) {
        if(path.length() == 0){
            return path;
        }
        String[] com = path.split("/");
        Stack<String> stack = new Stack();
        for(String dir : com){
            if(dir.equals(".") || dir.isEmpty()){
                continue;
            }
            if(dir.equals("..")){
                if(! stack.isEmpty()){
                    stack.pop();
                }
            }else{
                stack.push(dir);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(String dir : stack){
            sb.append("/");
            sb.append(dir);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }
}