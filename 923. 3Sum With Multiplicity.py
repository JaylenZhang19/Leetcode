class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        counter = collections.Counter(arr)
        keys = sorted(counter.keys())
        ans = 0
    
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += counter[x] * counter[y] * counter[z]
                    elif i == j < k:
                        ans += counter[x] * (counter[x] - 1) / 2 * counter[z]
                    elif i < j == k:
                        ans += counter[x] * counter[y] * (counter[y] - 1) / 2
                    else:  # i == j == k
                        ans += counter[x] * (counter[x] - 1) * (counter[x] - 2) / 6

                    j += 1
                    k -= 1


        return int(ans % mod)