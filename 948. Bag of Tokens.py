class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        ans = scores = 0
        while tokens and (P > tokens[0] or scores):
            while tokens and tokens[0] <= P:
                P -= tokens.pop(0)
                scores += 1
            ans = max(scores, ans)
            if tokens and scores:
                scores -= 1
                P += tokens.pop()
        return ans