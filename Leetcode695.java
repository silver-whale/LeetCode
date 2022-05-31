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
                    maxLand = Math.max(maxLand, count);
                }
            }
        }
        return maxLand;
    }

    public void dfs(int[][] grid, int r, int c)
}
