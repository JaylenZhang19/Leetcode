class Solution:
    def parseTernary(self, expression: str) -> str:
        
        def helper(left, right):
            if left == right:
                return expression[left:right+1]
            index = left + 2
            count = 0
            while index < right + 1:
                if expression[index] == '?':
                    count += 1
                elif expression[index] == ':':
                    count -= 1
                if count == -1:
                    break
                index += 1
            if expression[left] == 'T':
                return helper(left + 2, index-1)
            else:
                return helper(index+1, right)
        return helper(0, len(expression)-1)
            
                    