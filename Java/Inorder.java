package Java;

import java.util.ArrayList;
import java.util.List;

public class Inorder {
    public List<Integer> inorderTraversal(TreeNode root) {
        return inorder(root, new ArrayList<Integer>());
    }

    private List<Integer> inorder(TreeNode root, List<Integer> result) {
        if(root == null) {
            return result;
        }

        inorder(root.left, result);
        result.add(root.val);
        inorder(root.right, result);

        return result;
    }
}


 // Definition for a binary tree node.
class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}

