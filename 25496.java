import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        List<Integer> accessories = new ArrayList<>();

        int p = Integer.parseInt(str[0]);
        int n = Integer.parseInt(str[1]);
        int result = 0;

        String arr = br.readLine();

        for(String s : arr.split(" ")) {
            accessories.add(Integer.parseInt(s));
        }
        Collections.sort(accessories);

        for(int tired : accessories) {
            if(p >= 200){
                break;
            }else{
                p += tired;
                result += 1;
            }
        }

        System.out.println(result);
    }
}
