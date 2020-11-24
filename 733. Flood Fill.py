class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        column = len(image[0])
        preColor = image[sr][sc]
        queue = [[sr, sc]]
        image[sr][sc] = newColor
        if preColor == newColor:
            return image
        while queue:
            x, y = queue.pop(0)
            for x_, y_ in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newx, newy = x + x_, y + y_
                if 0 <= newx < row and 0 <= newy <column and image[newx][newy] == preColor:
                    image[newx][newy] = newColor
                    queue.append([newx, newy])
                
        return image
                    