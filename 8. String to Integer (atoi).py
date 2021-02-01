class Solution:
    def myAtoi(self, str: str) -> int:
        char_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        answer = None
        positive = 0
        negative = 0
        i = 0
        j = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        while j < len(char_num) and i < len(str):
            if answer == None and str[i] == '-':
                negative += 1
                i += 1
                continue
            if answer == None and str[i] == '+':
                positive += 1
                i += 1
                continue
            if str[i] == char_num[j]:
                answer = 0 if answer == None else 10 * answer
                answer += int(char_num[j])
                i += 1
                j = -1
            j += 1
        if answer == None:
            return 0
        if negative and positive:
            return 0
        if positive > 1 or negative > 1:
            return 0
        if negative:
            answer *= -1
        if answer > 2 ** 31 - 1:
            answer = 2 ** 31 - 1
        elif answer < -2 ** 31:
            answer = -2 ** 31
        return answer


s = "    -41"
answer = Solution().myAtoi(s)
print(answer)