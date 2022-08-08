class Leetcode117:
    def connect(self, root: 'Node') -> 'Node':
        nodes = {}

        def dfs(root, pointer):
            if not root:
                return
            if pointer in nodes:
                nodes[pointer].next = root
            nodes[pointer] = root
            root.next = None
            dfs(root.left, pointer+1)
            dfs(root.right, pointer+1)
        dfs(root, 0)

        return root