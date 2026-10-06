import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        // Please write your code here.

        int maxSum = 0;
        // 가로
        for (int i = 0; i<n; i++){
            for (int j = 0; j<m-2; j++){
                int tempSum = 0;
                tempSum += grid[i][j] + grid[i][j+1] + grid[i][j+2];
                maxSum = Math.max(maxSum, tempSum);
            }
        }
        for (int i = 0; i<n-2; i++){
            for (int j = 0; j<m; j++){
                int tempSum = 0;
                tempSum += grid[i][j] + grid[i+1][j] + grid[i+2][j];
                maxSum = Math.max(maxSum, tempSum);
            }
        }
        for (int i = 0; i<n-1; i++){
            for (int j = 0; j<m-1; j++){
                int tempSum =0;
                tempSum = grid[i][j] + grid[i][j+1] + grid[i+1][j+1];
                maxSum = Math.max(maxSum, tempSum);
                tempSum = grid[i][j] + grid[i+1][j] + grid[i+1][j+1];
                maxSum = Math.max(maxSum, tempSum);
                tempSum = grid[i][j] + grid[i][j+1] + grid[i+1][j];
                maxSum = Math.max(maxSum, tempSum);
                tempSum = grid[i+1][j+1] + grid[i][j+1] + grid[i+1][j];
                maxSum = Math.max(maxSum, tempSum);

            }
        }

        System.out.println(maxSum);

    
    }
}

