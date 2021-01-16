class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        n = len(people)
        right = n - 1
        ret = 0
        while left <= right:
            remain = limit
            count = 0
            while left <= right and (remain >= people[left] or remain >= people[right]) and count < 2:
                if people[right] <= remain:
                    remain -= people[right]
                    right -= 1
                    count += 1
                elif people[left] <= remain:
                    remain -= people[left]
                    left += 1
                    count += 1
                
            ret += 1
        return ret