import java.util.Scanner;

public class Main {
    static int n, m;
    static int[][] map;

    static int countGold (int cr, int cc, int k){
        int cnt = 0;

        for (int r=0; r<n; r++){
            for (int c=0; c<n; c++){
                if(Math.abs(r-cr)+Math.abs(c-cc)<=k){
                    cnt+=map[r][c];
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        map = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                map[i][j] = sc.nextInt();
        // Please write your code here.

        int ans = 0;

        for (int r=0; r<n; r++) {
            for (int c=0; c<n; c++) {
                for (int k=0; k<2*n; k++) {

                    int gold = countGold(r, c, k);
                    int cost = k*k + (k+1)*(k+1);

                    if (gold * m >= cost) {
                        ans = Math.max(ans, gold);
                    }
                }
            }
        }

        System.out.println(ans);


    }
}