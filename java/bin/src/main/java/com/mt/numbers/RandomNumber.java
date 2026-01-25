package numbers;
import java.util.Random;

public class RandomNumber {

	public static void main(String[] args) {
		// Random is a unmber generator
		Random random = new Random();
		
		int a = random.nextInt(100); // between [0,99]
		a += 1 ; // between [1,100]
		System.out.printf("random int : %d", a);
		
	}

}
