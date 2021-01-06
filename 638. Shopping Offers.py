class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        dp = {}
        def check(sp, need):
            flag = False
            for i, val in enumerate(sp[:len(need)]):
                if val > need[i]:
                    return False
                if val > 0 and need[i] > 0:
                    flag = True
            return flag
        
        def helper(need):
            ret = float('inf')
            key = tuple(need)
            if key in dp:
                return dp[key]
            for s in special:
                n = len(s)
                if check(s, need):
                    for i, num in enumerate(s[:n-1]):
                        need[i] -= num
                    ret = min(ret, helper(need) + s[-1])
                    for i, num in enumerate(s[:n-1]):
                        need[i] += num
            s = 0
            for i, num in enumerate(need):
                if num > 0:
                    s += num * price[i]
            ret = min(ret, s)
            dp[key] = ret
            return ret
        
        return helper(needs)
                