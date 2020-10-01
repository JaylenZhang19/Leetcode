class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set(wordDict)
        n = len(s)
        ans = False
        memo = {}
        def helper(start, index):
            if index == n:
                if s[start:index] in dic:
                    return True
                else:
                    return False
            if (start, index) in memo:
                return memo[(start, index)]
            case1, case2 = False, False
            if s[start:index] in dic:
                case1 = helper(index, index+1)
            case2 = helper(start, index + 1)
            memo[(start, index)] = case1 or case2
            return memo[(start, index)]
            
        return helper(0, 0)
        
        