package Java;

import java.util.LinkedList;
import java.util.Queue;

// BFS
// 1. 모든 0이 저장된 셀을 BFS 큐에 넣고, 1을 -1로 변경한다. 1로 쓸 경우 이 값이 결과값 1인지 저장값 1인지 알 수가 없음.
// 2. 만약 0 옆에 1이 있다면 이 역시 큐에 넣는다. 아까 우리가 0은 다 큐에 넣어줬는데 1의 경우 옆에 또 다른 1이 있을 수 있기 때문임.
// 즉, 0 셀을 싹 돌고, 1 셀을 싹 돈다.
public class Leetcode542 {
    public int[][] updateMatrix(int[][] mat) {

        if(mat == null || mat.length==0 || mat[0].length == 0) {return mat;}

        int m = mat.length;
        int n = mat[0].length;

        Queue<int[]> queue = new LinkedList<>();
        // down, right, up, left
        int[][] moves = new int[][] {{1,0}, {0,1}, {-1,0}, {0,-1}};


        // save index of 0s, change 1 to -1
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(mat[i][j]==0){
                    // 배열 생성 후 추가
                    queue.add(new int[]{i, j});
                }
                else{
                    mat[i][j] = -1;
                }
            }
        }

        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for(int[] move: moves){
                int newX = x + move[0];
                int newY = y + move[1];
                // 0 | -1 -> 1 옆에 0이 있으므로 1이 되어야 함, mat[x][y] + 1인 1이 들어감 -> 0 | 1
                // 0 | -1 | -1 -> 0 | 1 | -1 -> 0 | 1 | 2
                // 옆에 1이 없는 0은 어차피 필요가 없음 -> 최소거리의 0만 있으면 되기 때문.
                if(isValid(newX, newY, m, n) && mat[newX][newY] == -1){
                    queue.add(new int[]{newX, newY});
                    mat[newX][newY] = mat[x][y] + 1;
                }
            }
        }
        return mat;
    }

    private boolean isValid(int x, int y, int m, int n){
        return 0<=x && x<m && 0<=y && y<n;
    }
}

// DP

class P542{
    public int[][] updateMatrix2(int[][] mat){
        if(mat==null || mat.length == 0 || mat[0].length == 0) {return mat;}

        int m = mat.length;
        int n = mat[0].length;

        int[][] dp = new int[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(mat[i][j] == 0){
                    dp[i][j] = 0;
                }
                else{
                    dp[i][j] = Integer.MAX_VALUE - 1;
                }
            }
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i-1>=0){
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][j]+1);
                }
                if(j-1>=0){
                    dp[i][j] = Math.min(dp[i][j], dp[i][j-1] + 1);
                }
            }
        }

        for(int i=m-1; i>=0; i--){
            for(int j=n-1; j>=0; j--){
                if(i+1<m){
                    dp[i][j] = Math.min(dp[i][j], dp[i+1][j] + 1);
                }
                if(j+1<n){
                    dp[i][j] = Math.min(dp[i][j], dp[i][j+1]+1);
                }
            }
        }
        return dp;
    }
}


