import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main { 
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));    
        
        String x = br.readLine();
        int cnt = 0;        

        while(true) {            
            if(x.length() == 1){
                break;
            }
            int sum = 0;
            for(int i = 0; i < x.length(); i++) {
                sum += Integer.parseInt(String.valueOf(x.charAt(i)));
            }
            cnt++;
            x = String.valueOf(sum);
        }

        System.out.println(cnt);
        if(Integer.parseInt(x) % 3 == 0) {
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}
