package Java;

import java.util.LinkedList;
import java.util.Queue;

public class Leetcode994 {
    public int orangesRotting(int[][] grid){
        if(grid==null || grid.length == 0 || grid[0].length == 0) {return 0;}

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int row = grid.length, col = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();

        // get rotten orange's coordinate
        for(int i=0; i<row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        int count = 0;

        while(!queue.isEmpty()){
            // 한 번 전염되는 만큼만 꺼낼 것
            // Do not get every element in queue
            int size = queue.size();
            for(int s=0; s<size; s++){
                int[] curr = queue.poll();

                for(int d=0; d<4; d++){
                    int nr = curr[0] + dx[d];
                    int nc = curr[1] + dy[d];

                    if(isValid(grid, nr, nc)){
                        grid[nr][nc] = 2;
                        queue.add(new int[]{nr, nc});
                    }
                }
            }
            count += 1;
        }

        // If fresh orange remaining
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(grid[i][j] == 1) {return -1;}
            }
        }

        // count-1 because we added 1 in last recursion
        return count==0 ? 0 : count - 1;

    }

    public boolean isValid(int[][] grid, int i, int j){
        return i>=0 && i<grid.length && j>=0 && j<grid[0].length && grid[i][j] == 1;
    }
}
