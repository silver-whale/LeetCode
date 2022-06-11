package Java;

import java.util.LinkedList;
import java.util.Queue;

public class Leetcode695 {

    int count = 0;

    public int maxAreaOfIsland(int[][] grid){
        if(grid == null || grid.length == 0 || grid[0].length == 0) {return 0;}

        int row = grid.length, column = grid[0].length;
        int maxLand = 0;

        for(int r=0; r<row ; r++){
            for(int c=0; c<column; c++){
                if(grid[r][c] == 1){
                    count = 0;
                    dfs(grid, r, c);
                    // bfs(grid, r, c);
                    maxLand = Math.max(maxLand, count);
                }
            }
        }
        return maxLand;
    }

    public void dfs(int[][] grid, int r, int c){
        if(r<0 || c<0 || r>=grid.length || c>=grid[0].length || grid[r][c] == 0) {return;}
        count += 1;
        grid[r][c] = 0;
        dfs(grid, r-1, c);
        dfs(grid, r, c-1);
        dfs(grid, r+1, c);
        dfs(grid, r, c+1);
    }

    public void bfs(int[][] grid, int r, int c){
        int[] dr = {0, -1, 0, 1};
        int[] dc = {-1, 0, 1, 0};

        Queue<int[]> queue = new LinkedList<>();

        grid[r][c] = 0;
        count += 1;

        queue.add(new int[]{r, c});

        while(!queue.isEmpty()){
            // poll: get value from queue
            int[] temp = queue.poll();
            int tempR = temp[0];
            int tempC = temp[1];

            for(int i=0; i<4; i++){
                int curR = tempR + dr[i];
                int curC = tempC + dc[i];

                if(curR >=0 && curC >=0 && curR < grid.length && curC < grid[0].length && grid[curR][curC] == 1){
                    count += 1;
                    grid[curR][curC] = 0;
                    queue.add(new int[]{curR, curC});
                }
            }

        }

    }
}
