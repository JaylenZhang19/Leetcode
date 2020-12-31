class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        n = n1 + n2
        ret = [0] * n
        for index1, number1 in enumerate(reversed(num1)):
            for index2, number2 in enumerate(reversed(num2)):
                val = int(number1) * int(number2) + ret[n - (index1 + index2) - 1]
                add, mod = divmod(val, 10)
                ret[n - (index1 + index2) - 1] = mod
                advance = 1
                while add:
                    add += ret[n - (index1 + index2 + advance) - 1]
                    add, mod = divmod(add, 10)
                    ret[n - (index1 + index2 + advance) - 1] = mod
                    advance += 1

        left = 0
        while left < n and ret[left] == 0:
            left += 1
        return "".join(map(str, ret[left:])) if left < n else '0'