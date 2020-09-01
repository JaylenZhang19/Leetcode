class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        deep = 0
        tmp = label
        new_num = label
        while tmp:
            tmp //= 2
            deep += 1
        if deep % 2 == 0:
            first = 2 ** (deep - 1)
            last = 2 * first - 1
            new_num = first + (last - label)
        ret = []

        def helper(number, d):
            if d:
                if d % 2 == 1:
                    ret.insert(0, number)
                    helper(number // 2, d - 1)
                else:
                    f = 2 ** (d - 1)
                    l = f * 2 - 1
                    ret.insert(0, l - (number - f))
                    helper(number // 2, d - 1)
        helper(new_num, deep)
        return ret
            