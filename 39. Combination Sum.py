class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        self.combination(candidates, target, 0, temp, result)
        for i in result:
            i.sort()
        result.sort()
        i = 0
        while i < len(result) - 1:
            if result[i] == result[i + 1]:
                result.pop(i)
                i -= 1
            i += 1
        return result


    def combination(self, candidates, target, start, inList, result):
        if target == 0:
            result += [inList.copy()]
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            inList += [candidates[i]]
            self.combination(candidates, target - candidates[i], start, inList, result)
            inList.pop()
        
            

x = Solution()
print(x.combinationSum([2,3,5,7,4], 13))