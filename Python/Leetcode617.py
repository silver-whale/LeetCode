class Leetcode617:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            newNode = TreeNode(root1.val + root2.val)
            newNode.left = self.mergeTrees(root1.left, root2.left)
            newNode.right = self.mergeTrees(root1.right, root2.right)
            return newNode
        else:
            # 하나라도 없을 경우 값이 있는 것을 return
            return root1 or root2

        
        