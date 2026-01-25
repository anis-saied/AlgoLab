package numbers;

import java.util.Scanner;

public class ReadNumber {
	Scanner in = new Scanner(System.in);

	public double readDouble(String prompt) {

		// read double from console
		System.out.print(prompt);
		while (!in.hasNextDouble()) {
			String word = in.next();
			System.out.println(word + " is not a number");
			System.out.print(prompt);
		}
		double n = in.nextDouble();
		return n;
	}

	public int readInt(String prompt) {

		System.out.print(prompt);

		while (!in.hasNextInt()) {
			String word = in.next();
			System.out.println(word + " is not an integer");
			System.out.print(prompt);
		}
		int n = in.nextInt();
		return n;
	}

	public static void main(String[] args) {
		ReadNumber instance = new ReadNumber();
		double n = instance.readDouble("n=");
		System.out.println("double is = " + n);

		System.out.println("int is =" + instance.readInt("i="));

		instance.in.close();

	}
}
