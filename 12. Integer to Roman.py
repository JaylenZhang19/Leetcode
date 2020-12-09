class Solution:
    def intToRoman(self, num: int) -> str:
        table = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M']]
        s = str(num)
        n = len(s)
        ret = []
        for index, c in enumerate(s):
            position = n - index - 1
            if int(c) == 9:
                ret.append(table[position][0])
                ret.append(table[position+1][0])
            elif int(c) == 4:
                ret.append(table[position][0])
                ret.append(table[position][1])
            elif int(c) == 0:
                continue
            elif int(c) < 4:
                ret.append(int(c) * table[position][0])
            else:
                ret.append(table[position][1])
                ret.append((int(c)-5) * table[position][0])
            
        return "".join(ret)