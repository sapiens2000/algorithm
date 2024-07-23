import java.lang.reflect.Array;
import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        List<String> dict = new ArrayList<>();



        for(int i=1; i< str.length(); i++){
            for(int j=i+1;j<str.length(); j++){
                StringBuilder sb1 = new StringBuilder(str.substring(0, i));
                StringBuilder sb2 = new StringBuilder(str.substring(i, j));
                StringBuilder sb3 = new StringBuilder(str.substring(j));
                StringBuilder result = new StringBuilder(
                        sb1.reverse().append(
                                sb2.reverse().append(
                                        sb3.reverse()
                                )));
                dict.add(result.toString());
            }
        }
        Collections.sort(dict);
        System.out.println(dict.get(0));
    }

}
