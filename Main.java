import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		//현재 블록의 갯수가 1개면 추가된 블록의 수도 1개이기 때문에 A B 둘다 1로 저장
		int total = 1;
		int neededForUp = 1;
		

		int lvl = 1;
		
		//무한 루프
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
