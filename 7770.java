import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int total = 1;
		int neededForUp = 1;
		

		int lvl = 1;
		
		while(true) {
			neededForUp += 4 * lvl;
			total += neededForUp;
			if(total > n) {
				break;
			}
			lvl++;
		}
		System.out.println(lvl);
	}

}
