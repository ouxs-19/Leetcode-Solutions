class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        def adjacencyList():
            adj = defaultdict(list)
            for word in wordList:
                for i, _ in enumerate(word):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    adj[pattern].append(word)
            return adj
        def bfs(adj):
            reversedAdj = defaultdict(list)
            queue = deque([beginWord])
            visited = set([beginWord])
            while queue:
                visitedCurrentLevel = set()
                n = len(queue)
                for _ in range(n):
                    word = queue.popleft()
                    for i, _ in enumerate(word):
                        pattern = word[:i] + "*" + word[i + 1 :]
                        for nextWord in adj[pattern]:
                            if nextWord not in visited:
                                reversedAdj[nextWord].append(word)
                                if nextWord not in visitedCurrentLevel:
                                    queue.append(nextWord)
                                    visitedCurrentLevel.add(nextWord)
                visited.update(visitedCurrentLevel)
                if endWord in visited:
                    break
            return reversedAdj
        def dfs(reversedAdj, res, path):
            if path[0] == beginWord:
                res.append(list(path))
                return
            word = path[0]
            for nextWord in reversedAdj[word]:
                path.appendleft(nextWord)
                dfs(reversedAdj, res, path)
                path.popleft()
            return res

        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))

        return res
