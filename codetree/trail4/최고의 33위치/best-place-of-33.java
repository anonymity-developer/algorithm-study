import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        // Please write your code here.

        int max_coin = -1;
        for (int i= 0; i<n-2; i++){
            for(int j = 0; j<n-2; j++){
                int coin = 0;
                for (int k =0; k<3; k++){
                    coin += grid[i][j+k];
                    coin += grid[i+1][j+k];
                    coin += grid[i+2][j+k];
                }
                max_coin = Math.max(coin, max_coin);
            }
        }
        System.out.println(max_coin);
    }
}