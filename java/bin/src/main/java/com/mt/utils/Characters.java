package utils;

public class Characters {

	public static void main(String[] args) {
		// Alphabet
		System.out.println("Alphabet:");
		for (char c = 'a'; c < 'z'; c++) {
			System.out.printf("%2c", c);
		}
		
		StringUtils.newLine(2);
		
		// Greek alphabet
		System.out.println("Greek alphabet:");
		for (int i = 913; i < 937; i++) {
			System.out.printf("%2c",(char) i);
		}


	}

}
