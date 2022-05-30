public class Leetcode733 {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor){
        int color = image[sr][sc];
        // if (sr,sc) is not newColor
        if(color != newColor) {dfs(image, sr, sc, color, newColor);}
        return image;
    }

    public void dfs(int[][]image, int r, int c, int color, int newColor) {

        // find cells with same color with original one
        if (image[r][c] == color) {
            // Change color with new one
            image[r][c] = newColor;
            if (r >= 1) {
                dfs(image, r - 1, c, color, newColor);
            }
            if (c >= 1) {
                dfs(image, r, c - 1, color, newColor);
            }
            if (r + 1 < image.length) {
                dfs(image, r+1, c, color, newColor);
            }
            if(c+1 < image[0].length){
                dfs(image, r, c+1, color, newColor);
            }
        }
    }
}
