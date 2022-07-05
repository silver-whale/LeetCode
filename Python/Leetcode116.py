class Leetcode116:
    def connect(self, root):
        if not root or not root.left:
            return root
        
        root.left.next = root.right
        root.right.next = root.next.left if root.next else root.next

        self.connect(root.left)
        self.connect(root.right)   

        return root