import java.util.Scanner;
  
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        
        // Please write your code here.
        int happyArr = 0;
        for (int i = 0; i<n; i++){
            int curNum = 0;
            int curCon = 0;
            for (int j = 0; j<n; j++){
                if (curNum == grid[i][j]){
                    curCon += 1;
                } else{
                    curNum = grid[i][j];
                    curCon = 1;
                }
                if (curCon >= m) {
                    happyArr++;
                break;
                }
            }
        }
        for (int i = 0; i<n; i++){
            int curNum = 0;
            int curCon = 0;
            for (int j = 0; j<n; j++){
                if (curNum == grid[j][i]){
                    curCon += 1;
                } else{
                    curNum = grid[j][i];
                    curCon = 1;
                }
                if (curCon >= m) {
                    happyArr++;
                    break;
                }
            }
        }
        System.out.println(happyArr);

    }
}