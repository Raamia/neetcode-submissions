class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        adjlist = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i]+"_"+word[i+1:]
                if not temp in adjlist:
                    adjlist[temp] = []
                adjlist[temp].append(word)
        queue = deque()
        queue.append(beginWord)
        seen = set()
        seen.add(beginWord)
        count = 1
        while queue:
            lenq = len(queue)
            for i in range(lenq):
                word = queue.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    temp = word[:j]+"_"+word[j+1:]
                    for k in adjlist[temp]:
                        if not k in seen:
                            seen.add(k)
                            queue.append(k)
            count+=1
        return 0