class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        order = list(preorder.split(','))
        while order:
            stack.append(order.pop(0))
            while len(stack) > 2 and stack[-1] == "#" and stack[len(stack) - 2] == "#" and stack[len(stack) - 3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                if stack:
                    stack.append("#")
                
            if not stack:
                break
        if len(stack) == 1 and stack[0] == "#":
            return True
        if stack or order:
            return False
        return True
            