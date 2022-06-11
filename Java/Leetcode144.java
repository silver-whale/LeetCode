package Java;

import java.util.ArrayList;
import java.util.List;

public class Leetcode144 {
    List<Integer> answer = new ArrayList();
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root==null){
            return answer;
        }
        while(root!=null){
            answer.add(root.val);
            preorderTraversal(root.left);
            preorderTraversal(root.right);
            return answer;
        }
        return answer;
    }
}
