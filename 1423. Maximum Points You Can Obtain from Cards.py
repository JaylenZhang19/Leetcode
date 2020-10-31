# dynamic programming Time limit exceeded
def max_score(card_points, k):
    n = len(card_points)
    memo = {}

    def helper(begin, tail, k):
        if k == 0:
            return 0
        elif k > tail - begin + 1:
            return sum([card_points[begin:tail+1]])
        else:

            if (begin, tail, k) in memo:
                return memo[(begin, tail, k)]
            left = helper(begin+1, tail, k-1)
            right = helper(begin, tail-1, k-1)
            memo[(begin, tail, k)] = max(card_points[begin] + left, card_points[tail] + right)
            return memo[(begin, tail, k)]
    return helper(0, n-1, k)



# sliding windoow
def maxScore(self, card_points: List[int], k: int) -> int:
        n = len(card_points)
        chooses = sum(card_points[n-k:])
        ans = chooses
        for i in range(n-k, n):
            chooses = chooses - card_points[i] + card_points[i-(n-k)]
            ans = max(ans, chooses)
        return ans