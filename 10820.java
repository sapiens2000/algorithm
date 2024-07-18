import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        String str;

        while ((str = br.readLine()) != null) {
            int small = 0; 
            int capital = 0;   
            int number = 0; 
            int space = 0;  

            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                if (ch == ' ') space++;
                if (Character.isUpperCase(ch)) capital++;
                if (Character.isLowerCase(ch)) small++;
                if (Character.isDigit(ch)) number++;
            }
            sb.append(small + " " + capital + " " + number + " " + space + "\n");
        }
        System.out.print(sb);
    }
}
