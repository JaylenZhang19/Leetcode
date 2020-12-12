class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        ret = ""
        add_one = 0
        while p1 >= 0 and p2 >= 0:
            add_one, val = divmod(int(num1[p1]) + int(num2[p2]) + add_one, 10)
            ret = str(val) + ret
            p1 -= 1
            p2 -= 1
        while p1 >= 0:
            add_one, val = divmod(int(num1[p1]) + add_one, 10)
            ret = str(val) + ret
            p1 -= 1
        while p2 >= 0:
            add_one, val = divmod(int(num2[p2]) + add_one, 10)
            ret = str(val) + ret
            p2 -= 1
        if add_one:
            ret = "1" + ret
        return ret