class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ret = 0
        count = [0] * 26

        def helper(index):
            if index == len(arr):
                nonlocal ret
                ret = max(ret, sum(count))
            else:
                current_count = [0] * 26
                overlap = False
                for c in arr[index]:
                    if count[ord(c) - ord('a')] >= 1:
                        overlap = True
                        break
                    if current_count[ord(c) - ord('a')]:
                        overlap = True
                        break
                    else:
                        current_count[ord(c) - ord('a')] += 1


                if not overlap:
                    for c in arr[index]:
                        count[ord(c) - ord('a')] += 1
                    helper(index + 1)
                    for c in arr[index]:
                        count[ord(c) - ord('a')] -= 1
                helper(index + 1)

        helper(0)
        return ret
                        