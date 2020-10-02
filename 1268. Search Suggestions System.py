class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        mod = 10 ** 9
        s_list = []
        for c in searchWord:
            if not s_list:
                s_list.append(ord(c))
            else:
                 s_list.append((s_list[-1] * 26 + ord(c))%mod)
        
        n_w = len(searchWord)
        n_pro = len(products)
        ans = [[] for _ in range(n_w)]
        dp = [[0] * n_w for _ in range(n_pro)]
        for i in range(n_pro):
            for j in range(n_w):
                if j == 0:
                    dp[i][j] = ord(products[i][j])
                else:
                    if j >= len(products[i]):
                        continue
                    dp[i][j] = (dp[i][j - 1] * 26 + ord(products[i][j]))% mod
                if dp[i][j] == s_list[j]:
                    if len(ans) == j:
                        ans.append([])
                    ans[j].append(products[i])
        for i in range(len(ans)):
            ans[i].sort()
        return [row[:3] for row in ans]