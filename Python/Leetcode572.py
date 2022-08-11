class Leetcode572:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 값 비교
        def isSame(root, subRoot):
            # 둘 다 값이 없다
            if not root and not subRoot: return True
            # 하나만 값이 없다
            elif not root or not subRoot: return False
            return root.val==subRoot.val and isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)

        # 전체 트리 비교
        def traverse(root, subRoot):
            if not root and not subRoot: return True
            elif not root or not subRoot: return False
            else:
                if root.val != subRoot.val:
                    return traverse(root.left, subRoot) or traverse(root.right, subRoot)
                else:
                    # 첫 값이 같을 때 그 아래에 달려있음
                    if traverse(root.left, subRoot) or traverse(root.right, subRoot):
                        return True
                    # 첫 값부터 바로 달려있음
                    else:
                        return isSame(root, subRoot)
        
        return traverse(root,subRoot)

# s.val != t.val일 때는 무조건 아래를 탐색
# s.val == t.val일 때는 아래를 탐색 or 그 부분 탐색