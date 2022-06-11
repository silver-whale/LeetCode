# input : n, connections : [시작노드, 끝노드]

class Solution:
    # List[List[int]] : int형의 2차원 배열
    def minReorder(self, n:int, connections:List[List[int]]) -> int:
        edges = { (a,b) for a, b in connections}
        # city:[]는 딕셔너리임. key는 city, value는 배열
        neighbors = {city:[] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            # nonlocal : 지역변수가 아님을 선언, 한 단계 바깥쪽에 위치한 변수와 바인딩
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes