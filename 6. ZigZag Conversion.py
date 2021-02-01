class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = []
        temp = []
        i = 0
        count = 0
        while i < len(s):
            if count < numRows:
                temp.append(s[i])
                i = i + 1
                count += 1
                continue
            else:
                zigzag.append(temp)
                for j in range(numRows - 2):
                    temp = []
                    for k in range(numRows):
                        temp.append(" ")
                    if i < len(s):
                        temp[numRows - 2 - j] = s[i]
                    else:
                        break
                    zigzag.append(temp)
                    i = i + 1
                if i < len(s):
                    temp = [s[i]]
                    i = i + 1
                else:
                    break
                count = 1
                continue
        while len(temp) < numRows:
            temp.append(" ")
        if temp[0] != " ":
            zigzag.append(temp)

        answer = ""
        for j in range(numRows):
            temp = []
            for k in zigzag:
                if k[j] != " ":
                    answer += k[j]

        return answer


answer = Solution().convert("abcd", 3)
print(answer)
