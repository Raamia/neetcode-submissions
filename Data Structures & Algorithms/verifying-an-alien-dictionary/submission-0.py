class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if word1 == word2:
                continue
            wordlen = min(len(word1), len(word2))
            for s in range(wordlen):
                print(word1[s], word2[s])
                if order.index(word1[s]) > order.index(word2[s]):
                    return False
                if order.index(word1[s]) < order.index(word2[s]):
                    break
                if s == wordlen-1 and order.index(word1[s]) == order.index(word2[s]):
                    return len(word1) < len(word2)
        return True