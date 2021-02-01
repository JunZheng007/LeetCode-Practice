class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        return deck



test = [17,13,11,2,3,5,7]
answer = Solution().deckRevealedIncreasing(test)
print(answer)