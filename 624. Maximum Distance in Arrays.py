class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest, sec_smallest = float('inf'), float('inf')
        s_index, sces_index = -1, -1
        largest, sec_largest = float('-inf'), float('-inf')
        l_index, scel_index = -1, -1
        for i in range(len(arrays)):
            if arrays[i][0] < smallest:
                smallest, sec_smallest = arrays[i][0], smallest
                s_index, sces_index = i, s_index
            elif arrays[i][0] < sec_smallest:
                sec_smallest = arrays[i][0]
                sces_index = i
            if arrays[i][-1] > largest:
                largest, sec_largest = arrays[i][-1], largest
                l_index, scel_index = i, l_index
            elif arrays[i][-1] > sec_largest:
                sec_largest = arrays[i][-1]
                scel_index = i
        print(smallest, sec_smallest, largest, sec_largest)
        if s_index != l_index:
            return largest - smallest
        else:
            return max(largest - sec_smallest, sec_largest - smallest)