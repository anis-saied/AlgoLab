package utils;

public class StringUtils {

	public static void newLine() {
		// the method with less parameters call the method having more parameters
		newLine(1);
	}
	
	public static void newLine(int n) {
		do {
			System.out.println();
			n--;
		} while (n > 0);
	}

	public static void print(String prompt) {
		System.out.print(prompt);
	}
	
	
	public static void println(String prompt) {
		System.out.println(prompt);
	}
	
	public static void operators() {
		char c = '0';
		c++;
		System.out.println(c);
		c=(char) (c+1);
		System.out.println(c);
	}
	
	public static void main(String[] args) {
		System.out.println("first paragraph");
		StringUtils.newLine();
		System.out.println("second paragraph");
		StringUtils.operators();
	}
	
}
