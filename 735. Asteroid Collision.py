class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        for index, size in enumerate(nums):
            if size > 0:
                stack.append(size)
            else:
                add = True
                while stack and stack[-1] > 0:
                    if stack[-1] > (-size):
                        add = False
                        break
                    elif stack[-1] == (-size):
                        add = False
                        stack.pop()
                        break
                    else:
                        stack.pop()
                if add:
                    stack.append(size)
        return stack