def optimal(a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    left, right = 0, len(b) - 1
    diff = float('inf')
    ans = []
    while left < len(a) and right >= 0:
        index1, val1 = a[left]
        index2, val2 = b[right]
        if target - val1 - val2 == diff:
            ans.append([index1, index2])
        elif val1 + val2 <= target and target - val1 - val2 < diff:
            ans = [[index1, index2]]
            diff = target - val1 - val2
        if val1 + val2 > target:
            right -= 1
        else:
            left += 1
    return ans