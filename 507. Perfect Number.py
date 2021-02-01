import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                sum += num / i
        if sum == num:
            return True
        else:
            return False

num = 6
print(Solution().checkPerfectNumber(num))