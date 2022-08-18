class Leetcode117:
    def connect(self, root: 'Node') -> 'Node':
        depth = {}

        # d는 depth
        # 만약 해당 depth의 맨 첫 노드가 입력된다면(not in depth)
        # 키 d는 해당 노드가 먹음
        # 이후에 입력되는 노드들은 같은 층에 있는 뒤쪽 노드들이기 때문에 뒤에 달림
        def dfs(root, d):
            if not root: return
            if d in depth:
                depth[d].next = root
            depth[d] = root
            root.next = None
            dfs(root.left, d+1)
            dfs(root.right, d+1)
        
        dfs(root, 0)
        return root