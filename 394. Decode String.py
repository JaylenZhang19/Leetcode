class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmp = []
                i = len(stack) - 1
                while i >= 0:
                    if stack[i] != '[':
                        tmp.insert(0, stack[i])
                        stack.pop()
                    else:
                        stack.pop()
                        break
                    i -= 1
                times = []
                i = len(stack) - 1
                while i >= 0:
                    if ord('0') <= ord(stack[i]) <= ord('9'):
                        times.insert(0, stack[i])
                        stack.pop()
                    else:
                        break
                    i -= 1
                if times:
                    tmp = int("".join(times)) * tmp
                while tmp:
                    stack.append(tmp.pop(0))
        return "".join(stack)