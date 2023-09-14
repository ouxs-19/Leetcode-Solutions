class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        target = len(tickets) + 1
        seen = set()
        conds = set()
        path = []
        tickets.sort(reverse=True)

        for deb, fin in tickets:
            graph[deb].append(fin)

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            path.insert(0, start)


        dfs("JFK")
        return path