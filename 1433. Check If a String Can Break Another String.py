class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = []
        l2 = []
        n = len(s1)
        index = 0
        while index < n:
            l1.append(s1[index])
            l2.append(s2[index])
            index += 1
        l1.sort()
        l2.sort()
        l1_check = []
        l2_check = []
        for index in range(n):
            if l1[index] == l2[index]:
                l1_check.append(1)
                l2_check.append(1)
            elif l1[index] > l2[index]:
                l1_check.append(1)
                l2_check.append(0)
            else:
                l1_check.append(0)
                l2_check.append(1)
        print(l1_check, l2_check)
        if sum(l1_check) == n or sum(l2_check) == n:
            return True
        return False
    