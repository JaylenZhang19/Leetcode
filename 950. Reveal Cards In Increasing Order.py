class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ret = []
        while deck:
            current = deck.pop()
            if ret:
                rear = ret.pop()
                ret.insert(0, rear)
            ret.insert(0, current)
        return ret