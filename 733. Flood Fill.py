from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
            
        image[sr][sc] = newColor

        if sr > 0 and image[sr - 1][sc] == oldColor:
            Solution().floodFill(image, sr - 1, sc, newColor)
        if sr < len(image) - 1 and image[sr + 1][sc] == oldColor:
            Solution().floodFill(image, sr + 1, sc, newColor)
        if sc > 0 and image[sr][sc - 1] == oldColor:
            Solution().floodFill(image, sr, sc - 1, newColor)
        if sc < len(image[sr]) - 1 and image[sr][sc + 1] == oldColor:
            Solution().floodFill(image, sr, sc + 1, newColor)
        
        return image
        



image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1
print(Solution().floodFill(image, sr, sc, newColor))