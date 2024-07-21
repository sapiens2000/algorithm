import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        boolean[][] check = new boolean[n+1][n+1];

        for(int i=0;i<m;i++){
            input = br.readLine().split(" ");
            int n1 = Integer.parseInt(input[0]);
            int n2 = Integer.parseInt(input[1]);

            check[n1][n2] = true;
            check[n2][n1] = true; 
        }

        int answer = 0;
        // 아이스크림 조합을 뽑고 (2차원 배열)
        // 조합 체크
        for(int i=1;i<=n;i++){
            for(int j=i+1;j<=n;j++){
                if(check[i][j] == false){
                    for (int k=j+1;k<=n; k++) {
                        if(check[i][k] == false && check[j][k] == false) answer++;
                    }                    
                }

            }
        }
        System.out.println(answer);
    }
}
