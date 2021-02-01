from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        length = 0
        width = 0
        for i in range(int(math.sqrt(area)), 1, -1):
            if area % i == 0:
                width = i
                length = int(area / i)
                return [length, width]

        if width == 0:
            return [area, 1]


area = 1
print(Solution().constructRectangle(area))