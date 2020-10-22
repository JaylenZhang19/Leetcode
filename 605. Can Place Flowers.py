class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        for index, v in enumerate(flowerbed):
            if v == 0:
                if (index == 0 or flowerbed[index - 1] == 0) and (index == length - 1 or flowerbed[index + 1] == 0):
                    count +=1
                    flowerbed[index] = 1
        return count >= n