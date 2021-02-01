class Solution:
    def lemonadeChange(self, bills) -> bool:
        change = [0, 0, 0]
        for i in range(0, len(bills)):
            if bills[i] == 5:
                change[0] += 1

            elif bills[i] == 10:
                change[1] += 1
                if change[0] > 0:
                    change[0] -= 1
                else:
                    return False

            else:
                change[2] += 1
                if change[0] > 0 and change[1] > 0:
                    change[0] -= 1
                    change[1] -= 1
                elif change[0] > 2:
                    change[0] -= 3
                else:
                    return False
            print(bills[i], change)
        return True
            



test = [5,5,10,10,20]
answer = Solution().lemonadeChange(test)
print(answer)
